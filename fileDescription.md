# Two Major Files:

Two files are described on this page: 
- Base Text of OGNT: <a href='https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT_BASE_TEXT.zip'>OpenGNT_BASE_TEXT.zip</a>
- Keyed Features and Mapping IDs: <a href='https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT_keyedFeatures.csv.zip'>OpenGNT_keyedFeatures.csv.zip</a>

# OpenGNT_BASE_TEXT.zip:

<b>Usage:</b>

- unzip the zip file to unpack "OpenGNT_version3.csv"
- open "OpenGNT_version3.csv" with a text editor
- locate columns of data, separated from one another with a [TAB] character.

<b>1st Column - OGNTsort</b>

This column contains sort numbers of all words of the base text of OGNT.

<b>2nd Column - TANTTsort</b>

This column of sort numbers represent the order of "M" variants in TANTT.<br>
These are important bridges for mapping key features in file <a href='https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT_keyedFeatures.csv.zip'>OpenGNT_keyedFeatures.csv.zip</a>.

<b>3rd Column - FEATURESsort1</b>

Sort numbers as in the first column of the file "<a href='https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT_keyedFeatures.csv.zip'>OpenGNT_keyedFeatures.csv</a>"

<b>4th Column - LevinsohnClauseID</b>

Clause ID assigned to each word, corresponding to main cluase features as keyed in "<a href='https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT_keyedFeatures.csv.zip'>OpenGNT_keyedFeatures.csv</a>"

<b>5th Column - 〔BGBsortI｜LTsort｜STsort〕</b>

1) <b>BGBsortI</b> = Sort number of BGB (inclusive) as in original "berean_tables5.xlsx".<br>
2) <b>LTsort</b> = Sort number of Literal Translation, LT, described below.<br>
3) <b>STsort</b> = Sort number of Study Translation, ST, described below.

<b>6th Column - 〔Book｜Chapter｜Verse〕</b>

1) <b>Book</b> = Book number, ranging from 40 to 66, representing books from Matthew to the book of Revelation.<br>
2) <b>Chpter</b> = Chapter number<br>
3) <b>Verse</b> = Verse number

<b>7th Column - 〔OGNTu｜OGNTa｜lexeme｜sn｜rmac〕</b>

1) <b>OGNTk</b> = Greek word of OGNT in <a href='https://greekcntr.org/downloads/NTGRG.pdf'>Koine Greek</a>; used with <a href='https://greekcntr.org/downloads/KoineGreek.ttf'>KoineGreek Font</a><br>
2) <b>OGNTu</b> = Greek word of OGNT in unaccented form<br>
3) <b>OGNTa</b> = Greek word of OGNT in accented form<br>
4) <b>lexeme</b> = Greek word of OGNT in lexical form<br>
5) <b>sn</b> = Extended Strong's number, according to conventions of <a href='https://github.com/tyndale/STEPBible-Data/blob/master/TBESG%20-%20Tyndale%20Brief%20lexicon%20of%20Extended%20Strongs%20for%20Greek%20-%20TyndaleHouse.com%20STEPBible.org%20CC%20BY-NC-ND.txt'>TBESG - Tyndale Brief lexicon of Extended Strongs for Greek</a><br>
6) <b>rmac</b> = Robinson's Morphological Analysis Codes, morphological analysis combining James Tauber's work in TANTT and data in Berean translation table

<b>8th Column - 〔BDAGentry｜EDNTentry｜MounceEntry｜GoodrickKohlenbergerNumbers｜LN-LouwNidaNumbers〕</b>

1) <b>BDAGentry</b> = Lexical entry for lookup in <i>A Greek-English Lexicon of the New Testament and Other Early Christian Literature, 3rd ed.</i><br>
2) <b>EDNTentry</b> = Lexical entry for lookup in <i>Eerdman's Exegetical Dictionary of the New Testament</i><br>
3) <b>MounceEntry</b> = Lexical entry for lookup in <i>Mounce's Greek NT dictionary</i><br>
4) <b>GoodrickKohlenbergerNumbers</b> = GK number for lookup in GK-keyed dictionary<br>
5) <b>LN-LouwNidaNumbers</b> = LN number for lookup in <i>Greek-English Lexicon of the New Testament based on Semantic Domains</i>.

<b>9th Column - 〔transSBLcap｜transSBL｜modernGreek｜Fonética_Transliteración〕</b>

1) <b>transSBLcap</b> = transliteration according to SBL's conventions; with capitalisation<br>
2) <b>transSBL</b> = transliteration according to SBL's conventions<br>
3) <b>modernGreek</b> = modern Greek pronunciation<br>
4) <b>Fonética_Transliteración</b> = modern Greek pronunciation with phonetic pronunciation in Spanish

<b>10th Column - 〔TBESG｜BIB｜BLB｜BSB｜Español〕</b>

1) <b>TBESG</b> = Tyndale House's glosses, taken from TBESG (context-insensitive)<br>
2) <b>IT</b> = Interlinear Translation (context-sensitive); <br>adapted from Berean Interlinear Bible, with changes made where OGNT is different from BGB.<br>
3) <b>LT</b> = Literal Translation (context-sensitive); <br>adapted from Berean Literal Bible, with changes made where OGNT is different from BGB.<br>
4) <b>ST</b> = Study Translation (context-sensitive); <br>adapted from Berean Study Bible, with changes made where OGNT is different from BGB.<br>
5) <b>Español</b> = Spanish literal translation

<b>11th Column - 〔PMpWord｜PMfWord〕</b>

1) <b>PMpWord</b> = punctuation mark(s) preceding the main word<br>
2) <b>PMfWord</b> = punctuation mark(s) following the main word<br>
<i>Remarks:</i> Punctuation marks were adapted from data available in <a href='https://github.com/tyndale/STEPBible-Data'>TANTT - Tyndale Amalgamated NT Tagged texts</a>.

<b>12th Column - 〔Note｜Mvar｜Mlexeme｜Msn｜Mrmac〕</b>

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

<b>1st Column - FEATURESsort1</b><br>
This sort number is used to sort word order (TANTT) mapped in GNT features.<br>
<br>
<b>2nd Column - FEATURESsort2</b><br>
This sort number is used to sort word order (OGNT) mapped in GNT features.<br>
<br>
<b>3rd Column - mapIDV2</b><br>
This is a set of mapping ID, used to map resources, e.g. check the 1st column in file, mapping <a href='https://github.com/eliranwong/OpenGNT/blob/master/mapping_LevinsohnGNTDF/OGNT_FullMapping_Levinsohn.csv.zip'>Levinsohn GNT discourse features</a> to OGNT.<br>
<br>
<b>4th Column - mapIDV1</b><br>
This is a old set of mapping ID, used to map an early version of TANTT's data.<br>
<br>
<b>5th Column - 〔book｜chapter｜verse〕</b><br>
1) Book number<br>
2) Chapter number<br>
3) Verse number<br>
<br>
<b>6th Column - 〔TANTTsort｜OpenTextWord_KEY〕</b><br>
1) <b>OGNTsort</b> - It is same as the "OGNTsort" in file <a href='https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT_BASE_TEXT.zip'>OpenGNT_BASE_TEXT.zip</a>; this number is used as a mapping id in this file, to map the base text of OGNT to various GNT features.<br>
2) <b>TANTTsort</b> - It is same as the "TANTTsort" in file <a href='https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT_BASE_TEXT.zip'>OpenGNT_BASE_TEXT.zip</a>; this number is used as a mapping id in this file, to map the base text of OGNT to various GNT features.<br>
3) <b>OpenTextWordID</b> - Base Word IDs for for mapping <a href='https://github.com/OpenText-org/GNT_annotation_v1.0' target='_blank'>OpenText.org Linguisitc Annotation of the Greek New Testament</a>'s data<br> (Remarks: OpenText's GNT annotations places shorter ending of Mark 16 at the end of Mark 16:8 whereas OpenGNT places it at the end of Mark 16:20)<br><br>
<b>7th Column - Mapping to Levinsohn GNTDF's Data</b>: <br>
〔LevinsohnWordID｜noteMarker｜noteMarkerNoClause｜clause｜otQuotation｜reportedSpeech｜embeddedReportedSpeech〕<br>
1) <b>LevinsohnWordID</b> - Word IDs for mapping <a href='https://github.com/biblicalhumanities/levinsohn' target='_blank'>Levinsohn's GNT Discourse Features</a><br> <b>Full mapping is available in the file <a href='https://github.com/eliranwong/OpenGNT/blob/master/mapping_LevinsohnGNTDF/OGNT_FullMapping_Levinsohn.csv.zip'>OGNT_FullMapping_Levinsohn.csv.zip</a>.</b><br> (Remarks: Levinsohn's GNT Discourse Features places shorter ending of Mark 16 at the end of Mark 16:8 whereas OpenGNT places it at the end of Mark 16:20)<br>
2) <b>noteMarker</b> - Note marker, mapped to <a href='https://github.com/eliranwong/OpenGNT/blob/master/mapping_LevinsohnGNTDF/Levinsohn_notes.csv'>notes of Levinsohn's GNT Discourse Features</a><br>
3) <b>noteMarkerNoClause</b> - Note marker, mapped to <a href='https://github.com/eliranwong/OpenGNT/blob/master/mapping_LevinsohnGNTDF/Levinsohn_notes_withoutClauses.csv'>notes of Levinsohn's GNT Discourse Features [without clauses]</a><br>
4) <b>clause</b> - Clause markers, according to Levinsohn's GNT Discourse Features<br>
5) <b>clauseID</b> - ClauseID, assigned for each word<br>
6) <b>otQuotation</b> - Old Testament Quotations, according to Levinsohn's GNT Discourse Features [<ot> means "beginning of an OT quotation"; * means a word within an OT quotation; </ot> means "end of an OT quotation"; the slot is empty where it is not applicable.<br>
7) <b>reportedSpeech</b> - Reported speech, according to Levinsohn's GNT Discourse Features [<rs> means "beginning of a reported speech"; * means a word within a reported speech; </rs> means "end of a reported speech"; the slot is empty where it is not applicable.<br>
8) <b>embeddedReportedSpeech</b> - Embedded reported speech, according to Levinsohn's GNT Discourse Features [<ers> means "beginning of an embedded reported speech"; * means a word within an embedded reported speech; </ers> means "end of an embedded reported speech"; the slot is empty where it is not applicable.<br>
<br>
<b>8th Column - Corresponding TANTT data</b>: <br>
〔TANTT〕<br>
Corresponding TANTT data aligned with OGNT<br>
<br>
<b>9th Column - Gloss & Translation</b>: <br>
〔MounceGloss｜TyndaleHouseGloss｜OpenGNTGloss〕<br>
1) <b>MounceGloss</b> - English glosses (Context-<b>insensitive</b>) -<br>
English glosses selected from <a href='https://github.com/billmounce/dictionary'>Mounce's Concise Greek-English dictionary</a><br>
2) <b>TyndaleHouseGloss</b> - English glosses (Context-<b>insensitive</b>) -<br>
Generated from glosses of TBESG, produced by Tyndale House, Cambridge UK<br>
3) <b>OpenGNTGloss</b> - English glosses (Context-<b>sensitive</b>) -<br>
A full set of context-sensitive glosses for OpenGNT, worked out by Eliran Wong [initial data are drawn from "TyndaleHouseGloss" mentioned above; every gloss will be checked against its context; on-going updates are gradually integrated <a href='https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT.csv.zip'>HERE</a>; please check regularly]
<br><br>
<b><i>Remarks:</i></b><br>
- Lines / Entries starting with the following numbers are created for mapping purpose only (mapping resouces based on NA27, e.g. Levinsohn Discource Features):<br>
122580, 122586, 122796, 123928, 123948, 124712, 125108, 125238, 127544, 127800, 128058, 128061.
