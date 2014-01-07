This script downloads all of the files of the desired type(s) from web pages to corresponding directories.

The script is written in Python 2.7.5. It should work on any desktop operating system, but has only been tested with Ubuntu.

The types of file to download, the web pages to look at, and their corresponding directories are specified in personalize.csv.

I recommend that you edit personalize.csv in a spreadsheet program.

The second row, below 'types,' specifies the types of file to download. Enter the file extension without a period. Enter one file extension into each cell in the second row.

At the fifth row, below 'places,' begins the specification of web pages and corresponding directories. Specify the directory to which files should be sent in the first column. This directory name should begin and end with a forward slash. Specify the URL(s) in the other columns of the row corresponding to the proper directory. URLs should begin with 'http' and end with a forward slash.

This script is intended to download class materials from course web pages, but is usable for any similar purpose. I run it from a hotkey.

Desired features:
--Download materials from pages that are password-protected
