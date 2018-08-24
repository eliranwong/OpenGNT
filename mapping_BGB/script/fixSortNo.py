import re

inputFile = 'file.csv'
outputFile = 'file.csv'

f = open(inputFile,'r')
newData = f.read()
f.close()

# Greek unicode characters

newData = re.sub('^([0-9][0-9][0-9][0-9][0-9]\t)', r'0\1', newData, flags=re.M)
newData = re.sub('^([0-9][0-9][0-9][0-9]\t)', r'00\1', newData, flags=re.M)
newData = re.sub('^([0-9][0-9][0-9]\t)', r'000\1', newData, flags=re.M)
newData = re.sub('^([0-9][0-9]\t)', r'0000\1', newData, flags=re.M)
newData = re.sub('^([0-9]\t)', r'00000\1', newData, flags=re.M)

f = open(outputFile,'w')
f.write(newData)
f.close()