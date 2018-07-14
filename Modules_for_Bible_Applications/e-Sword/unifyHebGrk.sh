#! /usr/bin/sed -E -i .bak -f
#deal with Hebrew characters in A materials
s/שּׁ/שּׁ/g
s/שּׂ/שּׂ/g
s/אַ/אַ/g
s/אָ/אָ/g
s/בּ/בּ/g
s/גּ/גּ/g
s/דּ/דּ/g
s/הּ/הּ/g
s/וּ/וּ/g
s/זּ/זּ/g
s/טּ/טּ/g
s/יּ/יּ/g
s/ךּ/ךּ/g
s/כּ/כּ/g
s/לּ/לּ/g
s/מּ/מּ/g
s/נּ/נּ/g
s/סּ/סּ/g
s/פּ/פּ/g
s/צּ/צּ/g
s/קּ/קּ/g
s/רּ/רּ/g
s/תּ/תּ/g
#deal with Hebrew characters in L materials
s/ש(ְ|ֱ|ֲ|ֳ|ִ|ֵ|ֶ|ַ|ָ|ֹ|ֺ|ֻ)ׁ/שׁ\1/g
s/שׁ/שׁ/g
s/ש(ְ|ֱ|ֲ|ֳ|ִ|ֵ|ֶ|ַ|ָ|ֹ|ֺ|ֻ)ׂ/שׂ\1/g
s/שׂ/שׂ/g
#deal with Hebrew characters in A materials
s/ּ(ְ|ֱ|ֲ|ֳ|ִ|ֵ|ֶ|ַ|ָ|ֹ|ֺ|ֻ)/\1ּ/g
#deal with SHEBANQ 4b database (used the following command with CARE)
#s/וֹ/ֹו/g
#deal with Greek letters
s/ά/ά/g
s/ί/ί/g
s/έ/έ/g
s/ώ/ώ/g
s/ή/ή/g
s/ύ/ύ/g
s/ό/ό/g
s/̓͂Α/Ἆ/g
s/̓͂Η/Ἦ/g
s/̓͂Ω/Ὦ/g
s/ί̈/ΐ/g
s/ΐ/ΐ/g
s/ΰ/ΰ/g
s/᾿/ʼ/g
