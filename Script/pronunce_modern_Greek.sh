#! /usr/bin/sed -E -i .bak -f
# depends on what you need, the following first command may not be necessary in your case, please check
s/$/ /g
# convert diaeresis
s/[ϊΐῒϋΰῢ]/＊/g
# alphabet
s/[αΑἀἈἄἌᾄἂἆἎἁἉἅἍᾅἃἋάᾴὰᾶᾷᾳ]/a/g
s/[βΒ]/v/g
s/[γΓ]/g/g
s/[δΔ]/ð/g
s/[εΕἐἘἔἜἑἙἕἝἓἛέὲ]/e/g
s/[ζΖ]/z/g
s/[ηΗἠἨἤἬᾔἢἪἦἮᾖᾐἡἩἥἭἣἧᾗᾑήῄὴῆῇῃ]/iy/g
s/[θΘ]/θ/g
s/[ιἰἸἴἼἶἱἹἵἽἳἷίὶῖ]/iy/g
s/[κΚ]/k/g
s/[λΛ]/l/g
s/[μΜ]/m/g
s/[νΝ]/n/g
s/[ξΞ]/ks/g
s/[οΟὀὈὄὌὂὁὉὅὍὃὋόὸ]/o/g
s/[πΠ]/p/g
s/[ρΡῥῬ]/r/g
s/	r/	rh/g
s/[σςΣ]/s/g
s/s([vgðmnr])/z\1/g
# check if you need the following command
# s/s ([vgðmnr])/z \1/g
# check the word at the end of a line and the word at the beginning of next line, if necessary
s/[τΤ]/t/g
s/[υΥὐὔὒὖὑὙὕὝὓὗὟύὺῦ]/IY/g
s/[φΦ]/f/g
s/[χΧ]/kh/g
s/[ψΨ]/ps/g
s/[ωὠὤὬὢὦὮᾠὡὩὥὭὧὯᾧώῴὼῶῷῳ]/o/g
# diphthongs
s/aiy/e/g
s/eiy/iy/g
s/oiy/iy/g
s/IYiy/iy/g
s/oIY/u/g
s/aIY([pktfkθsz])/af\1/g
s/aIY/av/g
s/eIY([pktfkθsz])/ef\1/g
s/eIY/ev/g
s/iyIY([pktfkθsz])/iyf\1/g
s/iyIY/iyv/g
# change IY to small letter
s/IY/iy/g
# consonant clusters
s/gg/ngG/g
s/gk/ngG/g
s/gkh/ngkh/g
s/gks/ngks/g
s/mp([^ \.\(\)\[\]—,;·’⟦⟧⸂⸃⸄⸅⸀⸁12])/mb\1/g
s/nt([^ \.\(\)\[\]—,;·’⟦⟧⸂⸃⸄⸅⸀⸁12])/nd/g
# deal with letter ghama
s/ge/ye/g
s/giy/yiy/g
# change G to small letter
s/G/g/g
# restore diaeresis
s/＊/iy/g
s/ $//g
s/᾽//g
# reminder: read line 29
# replace s( \r[0-9]+?\t[vgðmnr]) with z\1 if necessary
