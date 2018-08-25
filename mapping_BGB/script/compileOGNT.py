# compile a NA-equivalent text from Berean Greek data (inclusive)

import re

inputFile = 'berean_tablesInclusive.csv'
outputFile = 'OGNT_v3.csv'

# open database
f = open(inputFile,'r')
newData = f.read()
f.close()

# clean up
newData = re.sub('^([^\n\t]*?\t)[^\n\t]*?\t[^\n\t]*?\t[^\n\t]*?\t[^\n\t]*?\t[^\n\t]*?\t[^\n\t]*?\t([^\n\t]*?\t[^\n\t]*?\t[^\n\t]*?\t)[^\n\t]*?\t([^\n\t]*?\t[^\n\t]*?\t[^\n\t]*?)\t.*?$', r'\1\2\3', newData, flags=re.M)
newData = re.sub('^[^\t\n]*?\t0\t0\t0\t.*?\n', '', newData, flags=re.M)

# take away some of TR variants; those variants are reserved in footnotes
newData = re.sub('^.*?{[^{}]*?}.*?\n', '', newData, flags=re.M)
# take away some of BYZ variants; those variants are reserved in footnotes
newData = re.sub('^.*?⧼[^⧼⧽]*?⧽.*?\n', '', newData, flags=re.M)
# take away some of WH variants; those variants are reserved in footnotes
newData = re.sub('^.*?\([^\(\)]*?\).*?\n', '', newData, flags=re.M)
# take away Nestle 1904 variants; those variants are reserved in footnotes
newData = re.sub('^.*?〈[^〈〉]*?〉.*?\n', '', newData, flags=re.M)
# take away some of SBLGNT variants; those variants are reserved in footnotes
newData = re.sub('^.*?〈[^〈〉]*?〉.*?\n', '', newData, flags=re.M)

# take away punctuation marks and variant markers
newData = re.sub('[ \-\—\,\;\:\?\.\·\·\'\‘\’\‹\›\“\”\«\»\(\)\[\]\{\}\⧼\⧽\〈\〉\*\‿\⇔\¦]᾽', '', newData)
newData = re.sub('[ \-\—\,\;\:\?\.\·\·\'\‘\’\‹\›\“\”\«\»\(\)\[\]\{\}\⧼\⧽\〈\〉\*\‿\⇔\¦]', '', newData)

# 2 lines below replace words in main text with variants, use for mapping purposes ONLY
#newData = re.sub('^([^\t\n]*?\t[^\t\n]*?\t[^\t\n]*?\t[^\t\n]*?\t)[^\t\n]*?\t([^\t\n]*?\t)([^\t\n＋＠＄]+?)$', r'\1\3\t\2\3', newData, flags=re.M)
#newData = re.sub('^([^\t\n]*?\t[^\t\n]*?\t[^\t\n]*?\t[^\t\n]*?\t[^\t\n]*?)\t.*?$', r'\1', newData, flags=re.M)
#newData = re.sub('[＊＝]｜', '', newData)

# put word order in first column
newData = re.sub('^([^\n\t]*?\t[0-9]+?\t[0-9]+?\t[0-9]+?\t[^\n\t]*?\t)([0-9]+?\t)', r'\2\1', newData, flags=re.M)

# close database
f = open(outputFile,'w')
f.write(newData)
f.close()

# sort word order
lines = open(outputFile, 'r').readlines()
f = open(outputFile, 'w')

for line in sorted(lines, key=lambda line: line.split()[0]):
    f.write(line)

f.close()
