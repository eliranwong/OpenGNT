# Two Major Files:

Two files are described on this page: 
- Base Text of OGNT: <a href='https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT_BASE_TEXT.zip'>OpenGNT_BASE_TEXT.zip</a>
- Keyed Features and Mapping IDs: <a href='https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT_keyedFeatures.csv.zip'>OpenGNT_keyedFeatures.csv.zip</a>

# OpenGNT_BASE_TEXT.zip:

<b>Usage:</b>

- unzip the zip file to unpack "OpenGNT_version3.csv"
- open "OpenGNT_version3.csv" with a text editor
- locate columns of data, separated from one another with a [TAB] character.

<b>1st Column - OGNT Sort Number</b>

This column contains sort numbers of all words.<br>
These sort numbers are also important bridges for mapping key features in file <a href='https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT_keyedFeatures.csv.zip'>OpenGNT_keyedFeatures.csv.zip</a>.

<b>2nd Column - BGBsort</b>

These are original sort numbers of Berean Greek Bible, BGB, available in Berean translation table.<br>
These numbers are important bridges to map associated data of Berean Greek Bible.

<b>3rd Column - 〔Book｜Chapter｜Verse〕</b>

Book = Book number, ranging from 40 to 66, representing books from Matthew to the book of Revelation.<br>
Chpter = Chapter number<br>
Verse = Verse number

<b>4th Column - 〔OGNTu｜OGNTa｜lexeme｜sn｜rmac〕</b>

OGNTu = Greek word of OGNT in unaccented form<br>
OGNTa = Greek word of OGNT in accented form<br>
lexeme = lexeme, sources from <a href='https://github.com/tyndale/STEPBible-Data/blob/master/TBESG%20-%20Tyndale%20Brief%20lexicon%20of%20Extended%20Strongs%20for%20Greek%20-%20TyndaleHouse.com%20STEPBible.org%20CC%20BY-NC-ND.txt'>TBESG - Tyndale Brief lexicon of Extended Strongs for Greek</a><br>
sn = Extended Strong's number, according to conventions of <a href='https://github.com/tyndale/STEPBible-Data/blob/master/TBESG%20-%20Tyndale%20Brief%20lexicon%20of%20Extended%20Strongs%20for%20Greek%20-%20TyndaleHouse.com%20STEPBible.org%20CC%20BY-NC-ND.txt'>TBESG - Tyndale Brief lexicon of Extended Strongs for Greek</a><br>
rmac = Robinson's Morphological Analysis Codes, morphological analysis combining James Tauber's work in TANTT and data in Berean translation table

000000	BGBsort	〔Book｜Chapter｜Verse〕	〔OGNTu｜OGNTa｜lexeme｜sn｜rmac〕	〔transSBL｜modernGreek〕	〔TBESG｜BIB｜BLB｜BSB〕	〔PMpWord｜PMfWord〕	〔Note｜Mvar｜Mlexeme｜Msn｜Mrmac〕

<br><br>
It gives users a quick access to the main text of OpenGNT, keyed to various features.
<br><br>
<a href='https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT.csv.zip'>This main text of OGNT </a> is currently <a href='https://github.com/eliranwong/OpenGNT/tree/master/CompareOGNTwithNA28'><b>the closest equivalent to the text of NA28</b></a>, made available for distribution under an open-license.
<br><br>
File format:
- each word of the main text is placed on a single line.<br>
- each line starts with a sort number in the whole text, followed by two different versions of mapping id (i.e. "mapIDV2" & "mapIDV1"), separated from one another by a [TAB] character,<br>
- followed by different groups of data, separated one another by a [TAB] character:<br>
<br>
- <b>Gropu I - Bible Reference</b>: <br>
〔book｜chapter｜verse〕<br>
1) Book number<br>
2) Chapter number<br>
3) Verse number<br>
<br>
- <b>Gropu II - Main text of OpenGNT</b>: <br>
〔unaccentedWord｜accentedWordV1｜accentedWordV2｜transliteration｜modernPronunciation〕<br>
1) unaccentedWord = Unaccented Word<br>
2) accentedWordV1 = Accented Word (version 1) - <a href='https://github.com/eliranwong/OpenGNT/tree/master/From_TANTT_to_OpenGNT'>details HERE</a><br>
3) transliteration = Transliteration<br>
4) modernPronunciation = Modern Greek Pronunciation<br>
<br>
- <b>Gropu III - Punctuation Marks</b>: <br>
〔puncMpWv1｜puncMfWv1｜puncMpWv2｜puncMfWv2〕<br>
1) puncMpWv1 = Punctuation mark(s), which precede(s) the main word (version 1)<br>
2) puncMfWv1 = Punctuation mark(s), which follow(s) the main word (version 1)<br>
<br>
- <b>Gropu IV - Mapping to OpenText.org Data</b>: <br>
〔OpenTextWordID〕<br>
1) <b>OpenTextWordID</b> - Base Word IDs for for mapping <a href='https://github.com/OpenText-org/GNT_annotation_v1.0' target='_blank'>OpenText.org Linguisitc Annotation of the Greek New Testament</a>'s data<br> (Remarks: OpenText's GNT annotations places shorter ending of Mark 16 at the end of Mark 16:8 whereas OpenGNT places it at the end of Mark 16:20)<br><br>
- <b>Gropu V - Mapping to Levinsohn GNTDF's Data</b>: <br>
〔LevinsohnWordID｜noteMarker｜noteMarkerNoClause｜clause｜otQuotation｜reportedSpeech｜embeddedReportedSpeech〕<br>
1) <b>LevinsohnWordID</b> - Word IDs for mapping <a href='https://github.com/biblicalhumanities/levinsohn' target='_blank'>Levinsohn's GNT Discourse Features</a><br> <b>Full mapping is available in the file <a href='https://github.com/eliranwong/OpenGNT/blob/master/mapping_LevinsohnGNTDF/OGNT_FullMapping_Levinsohn.csv.zip'>OGNT_FullMapping_Levinsohn.csv.zip</a>.</b><br> (Remarks: Levinsohn's GNT Discourse Features places shorter ending of Mark 16 at the end of Mark 16:8 whereas OpenGNT places it at the end of Mark 16:20)<br>
2) <b>noteMarker</b> - Note marker, mapped to <a href='https://github.com/eliranwong/OpenGNT/blob/master/mapping_LevinsohnGNTDF/Levinsohn_notes.csv'>notes of Levinsohn's GNT Discourse Features</a><br>
3) <b>noteMarkerNoClause</b> - Note marker, mapped to <a href='https://github.com/eliranwong/OpenGNT/blob/master/mapping_LevinsohnGNTDF/Levinsohn_notes_withoutClauses.csv'>notes of Levinsohn's GNT Discourse Features [without clauses]</a><br>
4) <b>clause</b> - Clause markers, according to Levinsohn's GNT Discourse Features<br>
5) <b>otQuotation</b> - Old Testament Quotations, according to Levinsohn's GNT Discourse Features [<ot> means "beginning of an OT quotation"; * means a word within an OT quotation; </ot> means "end of an OT quotation"; the slot is empty where it is not applicable.<br>
6) <b>reportedSpeech</b> - Reported speech, according to Levinsohn's GNT Discourse Features [<rs> means "beginning of a reported speech"; * means a word within a reported speech; </rs> means "end of a reported speech"; the slot is empty where it is not applicable.<br>
7) <b>embeddedReportedSpeech</b> - Embedded reported speech, according to Levinsohn's GNT Discourse Features [<ers> means "beginning of an embedded reported speech"; * means a word within an embedded reported speech; </ers> means "end of an embedded reported speech"; the slot is empty where it is not applicable.<br>
<br>
- <b>Gropu VI - Lexical Entries & Morphology</b>: <br>
〔lexeme｜BDAGentry｜EDNTentry｜MounceEntry｜morphologyCode｜morphologyDescription｜extendedStrongNumber｜GoodrickKohlenbergerNumbers｜LN-LouwNidaNumbers〕<br>
1) <b>lexeme</b> - lexeme<br>
2) <b>BDAGentry</b> - BDAG catchwords<br>
3) <b>EDNTentry</b> - EDNT catchwords<br>
4) <b>MounceEntry</b> - Entry words of <a href='https://github.com/billmounce/dictionary'>Mounce's Concise Greek-English dictionary</a><br>
5) <b>morphologyCode</b> - Robinson's Morphological Analysis Codes [RMAC]<br>
6) <b>morphologyDescription</b> - description on morphology<br>
7) <b>extendedStrongNumber</b> - Tyndale House's extended Strong's number<br>
8) <b>GoodrickKohlenbergerNumbers</b> - Goodrick-Kohlenberger numbers; compatible with <a href='https://github.com/billmounce/dictionary'>Mounce's Concise Greek-English dictionary</a><br>
9) <b>LouwNidaNumbers</b> - Louw-Nida numbers<br><br>
- <b>Gropu VII - Gloss & Translation</b>: <br>
〔MounceGloss｜TyndaleHouseGloss｜OpenGNTGloss｜NET2Words〕<br>
1) <b>MounceGloss</b> - English glosses (Context-<b>insensitive</b>) -<br>
English glosses selected from <a href='https://github.com/billmounce/dictionary'>Mounce's Concise Greek-English dictionary</a><br>
2) <b>TyndaleHouseGloss</b> - English glosses (Context-<b>insensitive</b>) -<br>
Generated from glosses of TBESG, produced by Tyndale House, Cambridge UK<br>
3) <b>OpenGNTGloss</b> - English glosses (Context-<b>sensitive</b>) -<br>
A full set of context-sensitive glosses for OpenGNT, worked out by Eliran Wong [initial data are drawn from "TyndaleHouseGloss" mentioned above; every gloss will be checked against its context; on-going updates are gradually integrated <a href='https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT.csv.zip'>HERE</a>; please check regularly]<br>
4) <b>NET2Words</b> - Words of The NET Bible® verse text (no Notes; 2nd Edition), mapped to OGNT [1st draft uploaded; subject to on-going revision]<br><br>
<a href='https://github.com/eliranwong/OpenGNT/blob/master/README.md#enhancement--forthcoming-additions'>Enhanced features</a> are gradually integrated in <a href='https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT.csv.zip'>this file</a>.
<br><br>
- <b>Gropu VIII - Textual Variants</b>: <br>
〔editionMarker1｜editionMarker2｜editions｜variants〕<br>
1) <b>editionMarker1</b> - a type of marker for details of editions, used in applications, e.g. BibleBento Plus<br>
2) <b>editionMarker2</b> - a type of marker for details of editions, used in applications, e.g. e-Sword<br>
3) <b>editions</b> - GNT editions having the same spelling as the main word of OpenGNT.  There may be variation in accentuation or capitalisation, though.  [B=Byzantine, I=NIV Greek, N=NA27, M=NA28 where words are different from NA27, R=Textus Receptus, S=SBLGNT, T=<a href='http://www.tyndalehouse.com/tregelles/' target='_blank'>Tregelles's GNT</a>, W=Westcott-Hort, H=<a href='https://www.thegreeknewtestament.com' target='_blank'>Tydale House GNT</a>]<br>
4) <b>variants</b> - variant(s), if any<br><br>
- <b>The last column - WordInHTML</b>: <br>
This last column provide words of OGNT in html format, with taggings on extended Strong's numbers, morphology, ot quotation [ot.../ot], reported speech [rs.../rs], embedded reported speech [ers.../ers], textual variant marker, Levinsohn's clause division & note marker, if applicable.<br><br>
<b><i>Remarks:</i></b><br>
- Lines / Entries starting with the following numbers are created for mapping purpose only (mapping resouces based on NA27, e.g. Levinsohn Discource Features):<br>
122580, 122586, 122796, 123928, 123948, 124712, 125108, 125238, 127544, 127800, 128058, 128061.<br>
These lines may not be relevant to compilation of the main text of OGNT.
