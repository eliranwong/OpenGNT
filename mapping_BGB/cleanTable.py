import re

inputFile = 'berean_tables.csv'
outputFile = 'berean_tablesInclusive.csv'

f = open(inputFile,'r')
newData = f.read()
f.close()

# clean up
newData = re.sub('\n[\n]+?([^\n])', r'\n\1', newData, flags=re.M)
newData = re.sub(' [ ]+?([^ ])', r' \1', newData, flags=re.M)
newData = re.sub('^ ', '', newData, flags=re.M)
newData = re.sub(' $', '', newData, flags=re.M)
newData = re.sub('\t ', '\t', newData, flags=re.M)
newData = re.sub(' \t', '\t', newData, flags=re.M)
newData = re.sub('^[^\n\t]*?\t[^\n\t]*?\t[^\n\t]*?\t[^\n\t]*?\t', '', newData, flags=re.M)
newData = re.sub('^[^\n\t]*?\t[^\n\t]*?\t[^\n\t]*?\t[^\n\t]*?\t[^\n\t]*?\t(BGB|BIB|BLB|BSB)\t.*?\n', '', newData, flags=re.M)
newData = re.sub('^([^\n\t]*?\t[^\n\t]*?\t[^\n\t]*?\t[^\n\t]*?\t[^\n\t]*?\t)[^\n\t]*?\t[^\n\t]*?\t[^\n\t]*?\t', r'\1', newData, flags=re.M)

# bookName to bookNo
newData = re.sub('\t[mM]atthew\|([0-9]+?):([0-9]+?)\t', r'\t40\t\1\t\2\t', newData)
newData = re.sub('\t[mM]ark\|([0-9]+?):([0-9]+?)\t', r'\t41\t\1\t\2\t', newData)
newData = re.sub('\t[lL]uke\|([0-9]+?):([0-9]+?)\t', r'\t42\t\1\t\2\t', newData)
newData = re.sub('\t[jJ]ohn\|([0-9]+?):([0-9]+?)\t', r'\t43\t\1\t\2\t', newData)
newData = re.sub('\t[aA]cts\|([0-9]+?):([0-9]+?)\t', r'\t44\t\1\t\2\t', newData)
newData = re.sub('\t[rR]omans\|([0-9]+?):([0-9]+?)\t', r'\t45\t\1\t\2\t', newData)
newData = re.sub('\t1\|[cC]orinthians\|([0-9]+?):([0-9]+?)\t', r'\t46\t\1\t\2\t', newData)
newData = re.sub('\t2\|[cC]orinthians\|([0-9]+?):([0-9]+?)\t', r'\t47\t\1\t\2\t', newData)
newData = re.sub('\t[gG]alatians\|([0-9]+?):([0-9]+?)\t', r'\t48\t\1\t\2\t', newData)
newData = re.sub('\t[eE]phesians\|([0-9]+?):([0-9]+?)\t', r'\t49\t\1\t\2\t', newData)
newData = re.sub('\t[pP]hilippians\|([0-9]+?):([0-9]+?)\t', r'\t50\t\1\t\2\t', newData)
newData = re.sub('\t[cC]olossians\|([0-9]+?):([0-9]+?)\t', r'\t51\t\1\t\2\t', newData)
newData = re.sub('\t1\|[tT]hessalonians\|([0-9]+?):([0-9]+?)\t', r'\t52\t\1\t\2\t', newData)
newData = re.sub('\t2\|[tT]hessalonians\|([0-9]+?):([0-9]+?)\t', r'\t53\t\1\t\2\t', newData)
newData = re.sub('\t1\|[tT]imothy\|([0-9]+?):([0-9]+?)\t', r'\t54\t\1\t\2\t', newData)
newData = re.sub('\t2\|[tT]imothy\|([0-9]+?):([0-9]+?)\t', r'\t55\t\1\t\2\t', newData)
newData = re.sub('\t[tT]itus\|([0-9]+?):([0-9]+?)\t', r'\t56\t\1\t\2\t', newData)
newData = re.sub('\t[pP]hilemon\|([0-9]+?):([0-9]+?)\t', r'\t57\t\1\t\2\t', newData)
newData = re.sub('\t[hH]ebrews\|([0-9]+?):([0-9]+?)\t', r'\t58\t\1\t\2\t', newData)
newData = re.sub('\t[jJ]ames\|([0-9]+?):([0-9]+?)\t', r'\t59\t\1\t\2\t', newData)
newData = re.sub('\t1\|[pP]eter\|([0-9]+?):([0-9]+?)\t', r'\t60\t\1\t\2\t', newData)
newData = re.sub('\t2\|[pP]eter\|([0-9]+?):([0-9]+?)\t', r'\t61\t\1\t\2\t', newData)
newData = re.sub('\t1\|[jJ]ohn\|([0-9]+?):([0-9]+?)\t', r'\t62\t\1\t\2\t', newData)
newData = re.sub('\t2\|[jJ]ohn\|([0-9]+?):([0-9]+?)\t', r'\t63\t\1\t\2\t', newData)
newData = re.sub('\t3\|[jJ]ohn\|([0-9]+?):([0-9]+?)\t', r'\t64\t\1\t\2\t', newData)
newData = re.sub('\t[jJ]ude\|([0-9]+?):([0-9]+?)\t', r'\t65\t\1\t\2\t', newData)
newData = re.sub('\t[rR]evelation\|([0-9]+?):([0-9]+?)\t', r'\t66\t\1\t\2\t', newData)


#change ^(.*?\t).*?\t.*?\t to \1
#change ^(.*?\t.*?\t).*?\t.*?\t.*?\t.*?\t to \1

# Greek unicode characters
newData = re.sub('ά', 'ά', newData)
newData = re.sub('ί', 'ί', newData)
newData = re.sub('έ', 'έ', newData)
newData = re.sub('ώ', 'ώ', newData)
newData = re.sub('ή', 'ή', newData)
newData = re.sub('ύ', 'ύ', newData)
newData = re.sub('ό', 'ό', newData)
newData = re.sub('̓͂Α', 'Ἆ', newData)
newData = re.sub('̓͂Η', 'Ἦ', newData)
newData = re.sub('̓͂Ω', 'Ὦ', newData)
newData = re.sub('ί̈', 'ΐ', newData)
newData = re.sub('ΐ', 'ΐ', newData)
newData = re.sub('ΰ', 'ΰ', newData)
newData = re.sub('[’᾿ʼ]', '᾽', newData)
newData = re.sub('ῇ', 'ῇ', newData)

f = open(outputFile,'w')
f.write(newData)
f.close()