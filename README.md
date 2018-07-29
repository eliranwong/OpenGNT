# OpenGNT
NA28 / NA27 Equivalent; Open Greek New Testament Resources

# Open Greek New Testament Project

Open Greek New Testament project aims to provide a bundle of high-quality and open-source materials on Greek New Testament for biblical studies.
<br><br>
An eclectic text, namely "Open Greek New Testament [OGNT]", is first produced as the base text for the rest of the project.  The text of OPNT is built upon <a href='https://github.com/eliranwong/OpenGNT/tree/master/From_TANTT_to_OpenGNT'>a group of high-quality scholarly materials</a>.  This aims to provide all bible students or scholars <b>a free text</b>, which is <a href='https://github.com/eliranwong/OpenGNT/tree/master/CompareOGNTwithNA28'><b>the closest equivalent to the text of NA28</b></a>, for studies or research purposes.

# Screenshot:

<img src="screenshot2.jpg">

# Main File:

"<a href='https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT.csv.zip'>OpenGNT.csv.zip</a>" is currently the main file for practical use. [<i>Remarks: Unzip the file before using it.</i>]
<br><br>
It gives users a quick access to the main text of OpenGNT, keyed to various features.
<br><br>
<a href='https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT.csv.zip'>This main text of OGNT </a> is currently <a href='https://github.com/eliranwong/OpenGNT/tree/master/CompareOGNTwithNA28'><b>the closest equivalent to the text of NA28</b></a>, made available for distribution under an open-license.
<br><br>
File format:
- each word of the main text is placed on a single line.<br>
- each line starts with an order number in the whole text, followed by an order number in a single verse, an unique OpenGNT id, separated from one another by a [TAB] character,<br>
- followed by different groups of data, separated one another by a [TAB] character:<br><br>
- <b>Gropu I - Bible Reference</b>: <br>
〔book｜chapter｜verse〕<br>
1) Book number<br>
2) Chapter number<br>
3) Verse number<br><br>
- <b>Gropu II - Main text of OpenGNT</b>: <br>
〔unaccentedWord｜accentedWord｜transliteration｜modernPronunciation〕<br>
1) Unaccented Word<br>
2) Accented Word<br>
3) Transliteration<br>
4) Modern Greek Pronunciation<br><br>
- <b>Gropu III - Mapping to OpenText.org Data</b>: <br>
〔OpenTextWordID〕<br>
1) <b>OpenTextWordID</b> - Base Word IDs for for mapping <a href='https://github.com/OpenText-org/GNT_annotation_v1.0' target='_blank'>OpenText.org Linguisitc Annotation of the Greek New Testament</a>'s data<br> (Remarks: OpenText's GNT annotations places shorter ending of Mark 16 at the end of Mark 16:8 whereas OpenGNT places it at the end of Mark 16:20)<br><br>
- <b>Gropu IV - Mapping to Levinsohn GNTDF's Data</b>: <br>
〔LevinsohnWordID｜noteMarker｜noteMarkerNoClause｜clause｜otQuotation｜reportedSpeech｜embeddedReportedSpeech〕<br>
1) <b>LevinsohnWordID</b> - Word IDs for mapping <a href='https://github.com/biblicalhumanities/levinsohn' target='_blank'>Levinsohn's GNT Discourse Features</a><br> <b>Full mapping is available in the file <a href='https://github.com/eliranwong/OpenGNT/blob/master/mapping_LevinsohnGNTDF/OGNT_FullMapping_Levinsohn.csv.zip'>OGNT_FullMapping_Levinsohn.csv.zip</a>.</b><br> (Remarks: Levinsohn's GNT Discourse Features places shorter ending of Mark 16 at the end of Mark 16:8 whereas OpenGNT places it at the end of Mark 16:20)<br>
2) <b>noteMarker</b> - Note marker, mapped to <a href='https://github.com/eliranwong/OpenGNT/blob/master/mapping_LevinsohnGNTDF/Levinsohn_notes.csv'>notes of Levinsohn's GNT Discourse Features</a><br>
3) <b>noteMarkerNoClause</b> - Note marker, mapped to <a href='https://github.com/eliranwong/OpenGNT/blob/master/mapping_LevinsohnGNTDF/Levinsohn_notes_withoutClauses.csv'>notes of Levinsohn's GNT Discourse Features [without clauses]</a><br>
4) <b>clause</b> - Clause markers, according to Levinsohn's GNT Discourse Features<br>
5) <b>otQuotation</b> - Old Testament Quotations, according to Levinsohn's GNT Discourse Features [<ot> means "beginning of an OT quotation"; * means a word within an OT quotation; </ot> means "end of an OT quotation"; the slot is empty where it is not applicable.<br>
6) <b>reportedSpeech</b> - Reported speech, according to Levinsohn's GNT Discourse Features [<rs> means "beginning of a reported speech"; * means a word within a reported speech; </rs> means "end of a reported speech"; the slot is empty where it is not applicable.<br>
7) <b>embeddedReportedSpeech</b> - Embedded reported speech, according to Levinsohn's GNT Discourse Features [<ers> means "beginning of an embedded reported speech"; * means a word within an embedded reported speech; </ers> means "end of an embedded reported speech"; the slot is empty where it is not applicable.<br>
<br>
- <b>Gropu V - Lexical Entries & Morphology</b>: <br>
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
- <b>Gropu VI - Gloss & Translation</b>: <br>
〔TyndaleHouseGloss｜MounceGloss｜NET2Words〕<br>
1) <b>TyndaleHouseGloss</b> - Tyndale House's English gloss; pronouns's sub-meanings worked out by Eliran wong<br>
2) <b>MounceGloss</b> - English glosses selected from <a href='https://github.com/billmounce/dictionary'>Mounce's Concise Greek-English dictionary</a><br>
3) <b>NET2Words</b> - Words of The NET Bible® verse text (no Notes; 2nd Edition), mapped to OGNT [will be uploaded later]<br><br>
<a href='https://github.com/eliranwong/OpenGNT/blob/master/README.md#enhancement--forthcoming-additions'>Enhanced features</a> are gradually integrated in this file.
<br><br>
- <b>Gropu VII - Textual Variants</b>: <br>
〔editionMarker1｜editionMarker2｜editions｜variants〕<br>
1) <b>editionMarker1</b> - a type of marker for details of editions, used in applications, e.g. BibleBento Plus<br>
2) <b>editionMarker2</b> - a type of marker for details of editions, used in applications, e.g. e-Sword<br>
3) <b>editions</b> - GNT editions having the same spelling as the main word of OpenGNT.  There may be variation in accentuation or capitalisation, though.  [B=Byzantine, I=NIV Greek, N=NA27, M=NA28 where words are different from NA27, R=Textus Receptus, S=SBLGNT, T=<a href='http://www.tyndalehouse.com/tregelles/' target='_blank'>Tregelles's GNT</a>, W=Westcott-Hort, H=<a href='https://www.thegreeknewtestament.com' target='_blank'>Tydale House GNT</a>]<br>
4) <b>variants</b> - variant(s), if any<br><br>
- <b>The last column - WordInHTML</b>: <br>
This last column provide words of OGNT in html format, with taggings on extended Strong's numbers, morphology, ot quotation [ot.../ot], reported speech [rs.../rs], embedded reported speech [ers.../ers], textual variant marker, Levinsohn's clause division & note marker, if applicable.<br><br>
<i>Remarks:</i><br>
- Lines / Entries starting with the following numbers are created for mapping purpose only (mapping resouces based on NA28, e.g. OpenText Linguistic Annotations version 1.0):<br>
48749, 81630, 93287, 100516, 105053o.<br>
- Lines / Entries starting with the following numbers are created for mapping purpose only (mapping resouces based on NA27, e.g. Levinsohn Discource Features):<br>
140392, 140400, 140639, 141940, 141964, 142836, 143281, 143431, 146071, 146370, 146668, 146673.

# License:

All files produced by this project are released under <a href='https://creativecommons.org/licenses/by-nd/4.0/legalcode' target='_blank'>CC BY-NC-ND 4.0 with additional specified relaxations</a>
<br><br>
You are allowed to use or distribute OpenGNT materials for non-commercial purpose (formatting is allowed, without changes in mapping data).
<br><br>
You are required to quote the following information, when any parts of OpenGNT materials are integrated in your own work or distributed:
<br><br>
<b>Open Greek New Testament Project</b><br>
Developer: Eliran Wong [<a href='https://biblebento.com/contact/contactform.php' target='_blank'>Contact</a>; <a href='https://biblebento.com/' target='_blank'>BibleBento.com</a>],<br>
Source at <a href='https://github.com/eliranwong/OpenGNT' target='_blank'>https://github.com/eliranwong/OpenGNT/</a>
<br><br>
[Remarks: Please include all links available in the credit information above.]
<br><br>
<b>Other Credits / Attributions:</b>
<br><br>
<b>TANTT data</b>:<br>
"Tyndale House, Cambridge" [<a href='www.TyndaleHouse.com' target='_blank'>www.TyndaleHouse.com</a>],<br>
and "STEP Bible" [<a href='www.STEPBible.org' target='_blank'>www.STEPBible.org</a>]<br>
and source at <a href='tyndale.github.io/STEPBible-Data/' target='_blank'>tyndale.github.io/STEPBible-Data/</a>
<br><br>
<b>The OpenText.org Syntactically Annotated Greek New Testament</b><br>
Stanley E. Porter<br>
Matthew Brook O'Donnell<br>
Jeffrey T. Reed<br>
Source: <a href='https://github.com/OpenText-org/GNT_annotation_v1.0' target='_blank'>GNT Annotation (version 1.0)</a><br>
This annotation was completed in 2006 and was made available for viewing on the OpenText.org website and also implemented in Logos bible search software.<br>
The annotation data has been migrated to a new, inline XML format by Christopher Land and the base text has been corrected and updated to the NA28 by Christopher Land and Ryder Wishart.
<br><br>
<b>Levinsohn's Greek New Testament Discourse Features</b><br>
Stephen Levinsohn's complete discourse features markup of the Greek New Testament (UBS4/NA27). This data was originally developed in BART and follow principles Levinsohn documented in his volume of Discourse Features of New Testament Greek.<br>
Source: <a href='https://github.com/biblicalhumanities/levinsohn'>https://github.com/biblicalhumanities/levinsohn</a><br>
©2016 SIL International<br>
<a href='https://github.com/biblicalhumanities/levinsohn/blob/master/LICENSE.md'>License</a><br>
Released by:<br>
Paul O'Rear<br>
Associate Coordinator<br>
International Translation<br>
SIL International
<br><br>
<b>NET Bible Copyright 2nd Edition (2017)</b><br>
NET BIble® Copyright THE NET BIBLE®, New English Translation (NET) Scripture quoted by permission. Quotations designated (NET) are from the NET Bible® copyright ©1996-2016 by Biblical Studies Press, L.L.C. <a href='http://netbible.com' target='_blank'>http://netbible.com</a> All rights reserved.  The names: THE NET BIBLE®, NEW ENGLISH TRANSLATION COPYRIGHT (c) 1996 BY BIBLICAL STUDIES PRESS, L.L.C. NET Bible® IS A  REGISTERED TRADEMARK THE NET BIBLE® LOGO, SERVICE MARK COPYRIGHT (c) 1997 BY BIBLICAL STUDIES PRESS, L.L.C. ALL RIGHTS RESERVEDSATELLITE IMAGERY COPYRIGHT (c) RØHR PRODUCTIONS LTD. AND CENTRE NATIONAL D'ÉTUDES SPATIALES PHOTOGRAPHS COPYRIGHT (c) RØHR PRODUCTIONS LTD.
<br>
The NET Bible® verse text (no Notes) can be used by anyone and integrated into your non-commercial  project or publication upon condition of proper Biblical Studies Press copyright and organizational acknowledgments ... (<a href='http://netbible.com/net-bible-copyright' target='_blank'>http://netbible.com/net-bible-copyright</a>)
<br><br>
<b>Mounce Concise Greek-English Dictionary</b><br>
Source: <a href='https://github.com/billmounce/dictionary'>https://github.com/billmounce/dictionary</a><br>
Used with the following attribution:<br>
Mounce Concise Greek-English Dictionary<br>
Copyright 1993 All Rights Reserved<br>
www.teknia.com/greek-dictionary
<br><br>
<b>Morphological Lexicon of the Greek New Testament</b><br>
Source: <a href='https://github.com/morphgnt/morphological-lexicon'>https://github.com/morphgnt/morphological-lexicon</a><br>
It is used to process data for mapping purpose.<br>


# Sources:

The base text of OpenGNT project, OGNT in short, is largely developed from a scholarly database, "TANTT - Tyndale Amalgamated NT Tagged texts".
<br><br>
Read in folder "<a href='https://github.com/eliranwong/OpenGNT/tree/master/From_TANTT_to_OpenGNT'>From_TANTT_to_OpenGNT</a>" for an introduction of TANTT and additional content, introduced by OpenGNT. 

# Comparison between OpenGNT and NA28

Read more in folder "<a href='https://github.com/eliranwong/OpenGNT/tree/master/CompareOGNTwithNA28'>CompareOGNTwithNA28</a>"

# Enhancement / Forthcoming additions:

- transliteration (according to SBL guide) - <a href='https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT.csv.zip'>DONE!</a><br>
- modern Greek pronunciation guide - <a href='https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT.csv.zip'>DONE!</a><br>
- an analytical lexicon containing all words of OpenGNT text - <a href='https://github.com/eliranwong/OpenGNT/blob/master/Lexicons/OGNT-Analytical_Lexicon.csv'>DONE!</a><br>
- sub-meanings on 5594 occurrences of αὐτός [he/she/it/self] - <a href='https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT.csv.zip'>DONE!</a><br>
- sub-meanings on 1387 occurrences of οὗτος [this/he/she/it] - <a href='https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT.csv.zip'>DONE!</a><br>
- sub-meanings on 2579 occurrences of ἐγώ [I/we] - <a href='https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT.csv.zip'>DONE!</a><br>
- sub-meanings on 1865 occurrences of σύ [you] - <a href='https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT.csv.zip'>DONE!</a><br>
- mapping GK numbers (mapped with <a href='https://github.com/billmounce/dictionary'>Mounce's Concise Greek-English dictionary</a>) - <a href='https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT.csv.zip'>First draft; CHECKING in progress</a><br>
- mapping Louw-Nida numbers (numbers only, not copyrighted materials) - <a href='https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT.csv.zip'>First draft; CHECKING in progress</a><br>
- mapping BDAG catchwords (catchwords only, not copyrighted materials) - <a href='https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT.csv.zip'>First draft; CHECKING in progress</a><br>
- mapping EDNT catchwords (catchwords only, not copyrighted materials) - <a href='https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT.csv.zip'>First draft; CHECKING in progress</a><br>
- mapping <a href='https://github.com/billmounce/dictionary' target='_blank'>Mounce's NT dictionary</a> - <a href='https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT.csv.zip'>DONE!</a><br>
- mapping <a href='https://github.com/OpenText-org/GNT_annotation_v1.0' target='_blank'>OpenText annotations</a> - <a href='https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT.csv.zip'>DONE!</a><br>
- creating a html template for visual presentation of OpenText annotations - <a href='https://github.com/eliranwong/OpenGNT/blob/master/mapping_OpenTextAnnotations/OpenText_v1_formatted_in_HTML.csv.zip'>DONE!</a><br>
- mapping <a href='https://github.com/biblicalhumanities/levinsohn' target='_blank'>Levinsohn's GNT Discourse Features</a> - <a href='https://github.com/eliranwong/OpenGNT/blob/master/OGNT_FullMapping_Levinsohn.csv.zip'>DONE!</a>; Full mapping is availalbe <a href='https://github.com/eliranwong/OpenGNT/blob/master/mapping_LevinsohnGNTDF/OGNT_FullMapping_Levinsohn.csv.zip'>HERE</a><br>
- tagging the text of OGNT with <a href='https://github.com/eliranwong/OpenGNT/blob/master/mapping_LevinsohnGNTDF/OGNT_FullMapping_Levinsohn.csv.zip'>Levinsohn GNT discourse features</a>, like <a href='https://github.com/biblicalhumanities/levinsohn/blob/master/LGNTDF/Main_clauses.xml'>main clauses</a>, <a href='https://github.com/biblicalhumanities/levinsohn/blob/master/LGNTDF/OT_quotes.xml'>OT quotations</a>, <a href='https://github.com/biblicalhumanities/levinsohn/blob/master/LGNTDF/Reported_Speech.xml'>reported speeches</a>, <a href='https://github.com/biblicalhumanities/levinsohn/blob/master/LGNTDF/EmbeddedRepSpeech.xml'>embedded reported speeches</a>, etc. - <a href='https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT.csv.zip'>DONE!</a><br>
- mapping "<a href='http://netbible.com/' target='_blank'>The NET Bible® verse text (no Notes) - 2nd Edition; New Testament</a>" (in progress)<br>
- mapping "Chinese Union Version"<br>
- more ... you are welcome to make suggestions at <a href='https://biblebento.com/contact/contactform.php' target='_blank'>https://biblebento.com/contact/contactform.php</a>

# Modules for Software Applications

Modules based on OpenGNT project are released gradually for use with bible applications.  They are made available in folder "<a href='https://github.com/eliranwong/OpenGNT/tree/master/Modules_for_Bible_Applications'>Modules_for_Bible_Applications</a>"
<br><br>
If you are a software developer and interested in this project, you are welcomed to contact <a href='https://biblebento.com/contact/contactform.php' target='_blank'>Eliran Wong</a>.
<br><br>
<img src="screenshot.jpg">

<img src="screenshot3.png">

