from urllib2 import urlopen
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

def download(place, website):
    html = urlopen(website).read()
    filelist = linkre.findall(html)
    

link = 'http://www.math.caltech.edu/~2013-14/2term/ma108b'
link2 = 'http://www.math.caltech.edu/~2013-14/2term/ma108b/hwk1.pdf'
url = urlopen(link)
text = url.read()

# search text for hrefsomething"something.pdf"
# get the link and set it as LINK
# get the name and set it as NAME. also add location info to the name

name = '/home/aaron/Dropbox/Caltech/WIN_2014/hwk1.pdf'
# urlretrieve(link2, name)

filelist = linkre.findall(text)
print filelist
