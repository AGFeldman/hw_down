from urllib2 import urlopen, HTTPError, URLError
from urllib import urlretrieve
import csv
import re

typesline = 1
placesline = 4

def isgood(entry):
    if entry == '':
        return False
    elif entry == ',':
        return False
    return True

with open('personalize.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    personal = list(csvreader)
    # personal is now a 2D list. access[row][column]

typeslist = []
reglist = []
for entry in personal[typesline]:
    if isgood(entry):
        typeslist.append(entry)
        reglist.append('href.*\".*' + entry + '\"')
finalreg = '|'.join(reglist)
linkre = re.compile(finalreg)
# linkre is now a regular expression that matches any html code snippet
# that is a link to a file of one of the types specified in personalize.csv

placeslist = []
for row in personal[placesline:]:
    place = row[0]
    if not isgood(place):
        continue
    webs = []
    for entry in row[1:]:
        if isgood(entry):
            webs.append(entry)
    placeslist.append((place, webs))
# placeslist is now a list of tuples
# (place on your computer, [list of web pages to scan there])

def checkretrieve(webpage, place):
    '''Checks if WEBPAGE exists. If it does, downloads it to PLACE.'''
    try:
        urlopen(webpage)
        urlretrieve(webpage, place)
    except HTTPError, e:
        None
    except URLError, e:
        None

def download(place, website):
    '''Downloads all of the desired file type from WEBSITE to PLACE.'''
    html = urlopen(website).read()
    filelist = linkre.findall(html)
    for file_ in filelist:
        firstquote = file_.find('\"')
        lastquote = file_.rfind('\"')
        lastslash = file_.rfind('/')
        beginname = max(firstquote, lastslash) + 1
        beginfileloc = firstquote + 1
        end = lastquote
        name = file_[beginname:end]
        longname = place + name
        fileloc = file_[beginfileloc:end]
        if fileloc[:4] == 'http':
            checkretrieve(fileloc, longname)
        else:
            checkretrieve(website + fileloc, longname)
    
for pair in placeslist:
    place = pair[0]
    websites = pair[1]
    for website in websites:
        download(place, website)

