# This file is created for merging latest work on OpenGNTGloss and NET2Words into main database file OpenGNT.csv

import re

inputFile = 'OpenGNTGloss_NET2Words_updating.csv'
outputFile = 'OpenGNTGloss_NET2Words.csv'
databaseFile = 'OpenGNT.csv'

# export latest glosses

f = open(inputFile,'r')
newData = f.read()
f.close()

newData = re.sub('^.*?｛([^｛｝]*?)｝\t〈([^｜]*?)｜.*?$', r'\2\t\1＊', newData, flags=re.M)
newData = re.sub('^.*?[^＊]\n', '', newData, flags=re.M)
newData = re.sub('＊', '', newData)

f = open(outputFile,'w')
f.write(newData)
f.close()

# insert latest glosses into database

f = open(databaseFile,'r')
oldData = f.read()
f.close()

newData = newData + oldData

f = open(databaseFile,'w')
f.write(newData)
f.close()

# sort data

lines = open(databaseFile, 'r').readlines()
f = open(databaseFile, 'w')

for line in sorted(lines, key=lambda line: line.split()[0]):
    f.write(line)

f.close()

# merge glosses

f = open(databaseFile,'r')
newData = f.read()
f.close()

newData = re.sub(r'^(.*?\t)(.*?)\n\1([^\n〔]*?〔[^\n〔]*?〔[^\n〔]*?〔[^\n〔]*?〔[^\n〔]*?〔[^\n〔]*?〔[^\n〔]*?〔[^\n｜]*?｜[^\n｜]*?｜)([^\n｜]*?｜[^\n｜]*?)〕', r'\1\3\2〕', newData, flags=re.M)

f = open(databaseFile,'w')
f.write(newData)
f.close()
