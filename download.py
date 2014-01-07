import re

from csv import reader
from os import path, stat
from time import strptime, mktime
from urllib2 import urlopen, URLError, HTTPError
from urllib import urlretrieve

typesline = 1
placesline = 4

check_for_new_version = True

def isgood(entry):
    if entry == '':
        return False
    elif entry == ',':
        return False
    return True

with open('personalize.csv', 'rb') as csvfile:
    csvreader = reader(csvfile, delimiter=',')
    personal = list(csvreader)
    # personal is now a 2D list. access[row][column]

typeslist = []
reglist = []
for entry in personal[typesline]:
    if isgood(entry):
        typeslist.append(entry)
        reglist.append('href.{0,5}\".*' + entry + '\"')
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
        print 'Downloaded a file to', place
    except HTTPError, e:
        None
    except URLError, e:
        None

def download(place, website):
    '''Downloads all of the desired file type from WEBSITE to PLACE.'''
    html = urlopen(website).read()
    # We delete html comments that have href in them. These are traps.
    html = re.sub(r'<!--.*href.*-->', '', html)
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
        if fileloc[:4] != 'http':
            fileloc = website + fileloc
        if not path.exists(longname):
            checkretrieve(fileloc, longname)
        elif check_for_new_version:
            url_handle = urlopen(fileloc)
            headers = url_handle.info()
            webmodtime_raw = headers.getheader('Last-Modified')
            if webmodtime_raw is None:
                checkretrieve(fileloc, longname)
            else:
                time_struct = strptime(webmodtime_raw, 
                                            '%a, %d %b %Y %H:%M:%S %Z')
                webmodtime = mktime(time_struct)
                mymodtime = stat(longname).st_mtime
                if mymodtime < webmodtime:
                    checkretrieve(fileloc, longname)

for pair in placeslist:
    place = pair[0]
    websites = pair[1]
    for website in websites:
        download(place, website)

print 'done'
