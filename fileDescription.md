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

<b>Book</b> = Book number, ranging from 40 to 66, representing books from Matthew to the book of Revelation.<br>
<b>Chpter</b> = Chapter number<br>
<b>Verse</b> = Verse number

<b>4th Column - 〔OGNTu｜OGNTa｜lexeme｜sn｜rmac〕</b>

<b>OGNTu</b> = Greek word of OGNT in unaccented form<br>
<b>OGNTa</b> = Greek word of OGNT in accented form<br>
<b>lexeme</b> = Greek word of OGNT in lexical form<br>
<b>sn</b> = Extended Strong's number, according to conventions of <a href='https://github.com/tyndale/STEPBible-Data/blob/master/TBESG%20-%20Tyndale%20Brief%20lexicon%20of%20Extended%20Strongs%20for%20Greek%20-%20TyndaleHouse.com%20STEPBible.org%20CC%20BY-NC-ND.txt'>TBESG - Tyndale Brief lexicon of Extended Strongs for Greek</a><br>
<b>rmac</b> = Robinson's Morphological Analysis Codes, morphological analysis combining James Tauber's work in TANTT and data in Berean translation table

<b>4th Column - 〔transSBL｜modernGreek〕</b>

<b>transSBL</b> = transliteration according to SBL's conventions<br>
<b>modernGreek</b> = modern Greek pronunciation

<b>5th Column - 〔TBESG｜BIB｜BLB｜BSB〕</b>

<b>TBESG</b> = Tyndale House's glosses, taken from TBESG (context-insensitive)<br>
<b>BIB</b> = translation from Berean Interlinear Bible (context-sensitive)<br>
<b>BLB</b> = translation from Berean Literal Bible (context-sensitive)<br>
<b>BSB</b> = translation from Berean Study Bible (context-sensitive)

<b>6th Column - 〔PMpWord｜PMfWord〕</b>

<b>PMpWord</b> = punctuation mark(s) preceding the main word<br>
<b>PMfWord</b> = punctuation mark(s) following the main word

<b>7th Column - 〔Note｜Mvar｜Mlexeme｜Msn｜Mrmac〕</b>

1) <b>Note</b> = Notes on a specific word<br>
(3 Types:<br>
'＋' means Greek word, which are not in original Berean Greek data, 3 words adapted from Byzantine text, 2 words adapted from BHP; <br>
'＊' means the main word is different from NA28; <br>
'＝' means the main word is identical to the corresponding word in NA28, with minor orthographical difference)<br>
2) <b>Mvar</b> = Greek variant in accented form, taken from TANTT database, applied only where '＊' or '＝' appear in 'Note' on the same row.<br>
3) <b>Mlexeme</b> = lexical form of the Greek variant, Mvar, applied only where '＊' or '＝' appear in 'Note' on the same row.<br>
4) <b>Msn</b> = Extended Strong's number of the Greek variant, Mvar, applied only where '＊' or '＝' appear in 'Note' on the same row.<br>
5) <b>Mrmac</b> = Robinson's Morphological Analysis Codes of the Greek variant, Mvar,, applied only where '＊' or '＝' appear in 'Note' on the same row.

# OpenGNT_keyedFeatures.csv.zip:

<b>Usage:</b>

- unzip the zip file to unpack "OpenGNT_keyedFeatures.csv"
- open "OpenGNT_keyedFeatures.csv" with a text editor
- locate columns of data, separated from one another with a [TAB] character.

<b>1st Column - Features Sort Number</b><br>
This sort number is used to sort word order mapped in GNT features.<br>
<br>
<b>2nd Column - mapIDV2</b><br>
This is a set of mapping ID, used to map resources like Levinsohn GNT discourse features.<br>
<br>
<b>3rd Column - mapIDV1</b><br>
This is a old set of mapping ID, used to map an early version of TANTT's data.<br>
<br>
<b>4th Column - 〔book｜chapter｜verse〕</b><br>
1) Book number<br>
2) Chapter number<br>
3) Verse number<br>
<br>
<b>5th Column - 〔OGNT_KEY｜OpenTextWord_KEY〕</b><br>
1) <b>OGNT_KEY</b> - It is same as the main sort number in file <a href='https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT_BASE_TEXT.zip'>OpenGNT_BASE_TEXT.zip</a>; this number is used as a mapping id in this file, to map the base text of OGNT to various GNT features.<br>
2) <b>OpenTextWordID</b> - Base Word IDs for for mapping <a href='https://github.com/OpenText-org/GNT_annotation_v1.0' target='_blank'>OpenText.org Linguisitc Annotation of the Greek New Testament</a>'s data<br> (Remarks: OpenText's GNT annotations places shorter ending of Mark 16 at the end of Mark 16:8 whereas OpenGNT places it at the end of Mark 16:20)<br><br>
<b>6th Column - Mapping to Levinsohn GNTDF's Data</b>: <br>
〔LevinsohnWordID｜noteMarker｜noteMarkerNoClause｜clause｜otQuotation｜reportedSpeech｜embeddedReportedSpeech〕<br>
1) <b>LevinsohnWordID</b> - Word IDs for mapping <a href='https://github.com/biblicalhumanities/levinsohn' target='_blank'>Levinsohn's GNT Discourse Features</a><br> <b>Full mapping is available in the file <a href='https://github.com/eliranwong/OpenGNT/blob/master/mapping_LevinsohnGNTDF/OGNT_FullMapping_Levinsohn.csv.zip'>OGNT_FullMapping_Levinsohn.csv.zip</a>.</b><br> (Remarks: Levinsohn's GNT Discourse Features places shorter ending of Mark 16 at the end of Mark 16:8 whereas OpenGNT places it at the end of Mark 16:20)<br>
2) <b>noteMarker</b> - Note marker, mapped to <a href='https://github.com/eliranwong/OpenGNT/blob/master/mapping_LevinsohnGNTDF/Levinsohn_notes.csv'>notes of Levinsohn's GNT Discourse Features</a><br>
3) <b>noteMarkerNoClause</b> - Note marker, mapped to <a href='https://github.com/eliranwong/OpenGNT/blob/master/mapping_LevinsohnGNTDF/Levinsohn_notes_withoutClauses.csv'>notes of Levinsohn's GNT Discourse Features [without clauses]</a><br>
4) <b>clause</b> - Clause markers, according to Levinsohn's GNT Discourse Features<br>
5) <b>otQuotation</b> - Old Testament Quotations, according to Levinsohn's GNT Discourse Features [<ot> means "beginning of an OT quotation"; * means a word within an OT quotation; </ot> means "end of an OT quotation"; the slot is empty where it is not applicable.<br>
6) <b>reportedSpeech</b> - Reported speech, according to Levinsohn's GNT Discourse Features [<rs> means "beginning of a reported speech"; * means a word within a reported speech; </rs> means "end of a reported speech"; the slot is empty where it is not applicable.<br>
7) <b>embeddedReportedSpeech</b> - Embedded reported speech, according to Levinsohn's GNT Discourse Features [<ers> means "beginning of an embedded reported speech"; * means a word within an embedded reported speech; </ers> means "end of an embedded reported speech"; the slot is empty where it is not applicable.<br>
<br>
<b>7th Column - Lexical Entries & Morphology</b>: <br>
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
- <b>8th Column - Gloss & Translation</b>: <br>
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
<b>9th Column - Textual Variants</b>: <br>
〔editionMarker1｜editionMarker2｜editions｜variants〕<br>
1) <b>editionMarker1</b> - a type of marker for details of editions, used in applications, e.g. BibleBento Plus<br>
2) <b>editionMarker2</b> - a type of marker for details of editions, used in applications, e.g. e-Sword<br>
3) <b>editions</b> - GNT editions having the same spelling as the main word of OpenGNT.  There may be variation in accentuation or capitalisation, though.  [B=Byzantine, I=NIV Greek, N=NA27, M=NA28 where words are different from NA27, R=Textus Receptus, S=SBLGNT, T=<a href='http://www.tyndalehouse.com/tregelles/' target='_blank'>Tregelles's GNT</a>, W=Westcott-Hort, H=<a href='https://www.thegreeknewtestament.com' target='_blank'>Tydale House GNT</a>]<br>
4) <b>variants</b> - variant(s), if any<br><br>
- <b>The last column - WordInHTML</b>: <br>
This last column provide words of OGNT in html format, with taggings on extended Strong's numbers, morphology, ot quotation [ot.../ot], reported speech [rs.../rs], embedded reported speech [ers.../ers], textual variant marker, Levinsohn's clause division & note marker, if applicable.<br><br>
<b><i>Remarks:</i></b><br>
- Lines / Entries starting with the following numbers are created for mapping purpose only (mapping resouces based on NA27, e.g. Levinsohn Discource Features):<br>
122580, 122586, 122796, 123928, 123948, 124712, 125108, 125238, 127544, 127800, 128058, 128061.
