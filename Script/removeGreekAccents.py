import re

inputFile = 'berean_accented.csv'
outputFile = 'berean_unaccented.csv'

f = open(inputFile,'r')
newData = f.read()
f.close()

# Greek unicode characters

searchReplace = (
    ('[ἀἄᾄἂἆἁἅᾅἃάᾴὰᾶᾷᾳ]', 'α'),
    ('[ἈἌἎἉἍἋ]', 'Α'),
    ('[ἐἔἑἕἓέὲ]', 'ε'),
    ('[ἘἜἙἝἛ]', 'Ε'),
    ('[ἠἤᾔἢἦᾖᾐἡἥἣἧᾗᾑήῄὴῆῇῃ]', 'η'),
    ('[ἨἬἪἮἩἭἫ]', 'Η'),
    ('[ἰἴἶἱἵἳἷίὶῖϊΐῒ]', 'ι'),
    ('[ἸἼἹἽ]', 'Ι'),
    ('[ὀὄὂὁὅὃόὸ]', 'ο'),
    ('[ὈὌὉὍὋ]', 'Ο'),
    ('[ῥ]', 'ρ'),
    ('[Ῥ]', 'Ρ'),
    ('[ὐὔὒὖὑὕὓὗύὺῦϋΰῢ]', 'υ'),
    ('[ὙὝὟ]', 'Υ'),
    ('[ὠὤὢὦᾠὡὥὧᾧώῴὼῶῷῳ]', 'ω'),
    ('[ὨὬὪὮὩὭὯ]', 'Ω'),
    ("[\-\—\,\;\:\\\?\.\·\·\'\‘\’\‹\›\“\”\«\»\(\)\[\]\{\}\⧼\⧽\〈\〉\*\‿\᾽\⇔\¦]", ""),
)
for search, replace in searchReplace:
    newData = re.sub(search, replace, newData)

f = open(outputFile,'w')
f.write(newData)
f.close()