from urllib2 import urlopen
from urllib import urlretrieve
import csv
import re

typesline = 1

with open('personalize.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    personal = list(csvreader)
    # personal is now a 2D list. access[row][column]

typeslist = []
reglist = []
for entry in personal[typesline]:
    if '' != entry != ',':
        typeslist.append(entry)
        reglist.append('href.*\".*' + entry + '\"')
finalreg = '|'.join(reglist)
print finalreg

p = re.compile(finalreg)

link = 'http://www.math.caltech.edu/~2013-14/2term/ma108b'
link2 = 'http://www.math.caltech.edu/~2013-14/2term/ma108b/hwk1.pdf'
url = urlopen(link)
text = url.read()

# search text for hrefsomething"something.pdf"
# get the link and set it as LINK
# get the name and set it as NAME. also add location info to the name

name = '/home/aaron/Dropbox/Caltech/WIN_2014/hwk1.pdf'
# urlretrieve(link2, name)

filelist = p.findall(text)
print filelist
