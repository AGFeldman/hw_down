from urllib2 import urlopen
from urllib import urlretrieve
import csv

with open('personalize.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    personal = list(csvreader)
    # personal is now a 2D list. access[row][column]

link = 'http://www.math.caltech.edu/~2013-14/2term/ma108b/hwk1.pdf'
link2 = 'http://www.math.caltech.edu/~2013-14/2term/ma108b'
url = urlopen(link2)
text = url.read()
# search text for hrefsomething"something.pdf"
# get the link and set it as LINK
# get the name and set it as NAME. also add location info to the name
name = '/home/aaron/Dropbox/Caltech/WIN_2014/hwk1.pdf'
# urlretrieve(link, name)
