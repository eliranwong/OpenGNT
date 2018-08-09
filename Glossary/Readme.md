These files are used for mapping data, building interlinear or vacabulary list, etc:

<b>File:</b> <a href='https://github.com/eliranwong/OpenGNT/blob/master/Glossary/OpenGNTGloss_NET2Words.csv'>OpenGNTGloss_NET2Words.csv</a> - 3 columns, separated one another by [TAB] characters:<br>
Word order used in the first column of <a href='https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT.csv.zip'>the Main Database File HERE</a> [TAB] Context-sensitive glosses for OpenGNT [TAB] mapping to words of NET2<br>
(subject to on-going revisions / corrections)<br>
<br>
<b>File:</b> <a href='https://github.com/eliranwong/OpenGNT/blob/master/Glossary/GK_lemma_EnglishGloss.csv'>GK_lemma_EnglishGloss.csv</a> - 3 columns, separated one another by [TAB] characters:<br>
GK number [TAB] lemma [TAB] English gloss<br>
Source: <a href='https://github.com/billmounce/dictionary'>https://github.com/billmounce/dictionary</a><br>
Credits:<br>
Mounce Concise Greek-English Dictionary<br>
Copyright 1993 All Rights Reserved<br>
www.teknia.com/greek-dictionary<br>
Oneline verson <a href='https://www.billmounce.com/greek-dictionary'>https://www.billmounce.com/greek-dictionary</a> is also consulted for entries which are not found in the above github source.<br>
Statement on the use of online version of Greek-English dictionary:<br>
"Our committment is that this dictionary will remain free, and we will be encouraging software companies to adopt it as their generic Greek-English dictionary." (This statement is quoted from the page at: <a href='https://www.billmounce.com/greek-dictionary'>https://www.billmounce.com/greek-dictionary</a>)<br><br>

<b>File:</b> <a href='https://github.com/eliranwong/OpenGNT/blob/master/Glossary/SN_lemma_EnglishGloss.csv'>eSN_lemma_EnglishGloss.csv</a> - 3 columns, separated one another by [TAB] characters:<br>
Extended Strong's number [TAB] lemma [TAB] English gloss<br>
Source: TBESG in <a href='https://github.com/tyndale/STEPBible-Data' target='_blank'>https://github.com/tyndale/STEPBible-Data</a><br>
Credits:<br>
"Tyndale House, Cambridge" [<a href='www.TyndaleHouse.com' target='_blank'>www.TyndaleHouse.com</a>],<br>
and "STEP Bible" [<a href='www.STEPBible.org' target='_blank'>www.STEPBible.org</a>]<br>
and source at <a href='https://github.com/tyndale/STEPBible-Data' target='_blank'>https://github.com/tyndale/STEPBible-Data/</a>

<hr>

Below is a template for updating OpenGNTGloss and mapping NET2 words.

<b>File:</b> <a href='https://github.com/eliranwong/OpenGNT/blob/master/Glossary/OpenGNTGloss_NET2Words_updating.csv.zip'>OpenGNTGloss_NET2Words_updating.csv.zip</a>

Latest data on "OpenGNTGloss" & "NET2Words" are exported to <a href='https://github.com/eliranwong/OpenGNT/blob/master/Glossary/OpenGNTGloss_NET2Words.csv'>OpenGNTGloss_NET2Words.csv</a> and integrated into <a href='https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT.csv.zip'>the main Database file</a>.

The 1st vertical column is order number.
Each verse starts with a verse text of NET2,
followed by lines of OpenGNT words, with features in the following format:

orderNumber	〔book｜chapter｜verse〕｛OpenGNTGloss｜NET2Words｝	〈orderNumber used in OpenGNT.csv｜mainWord of OGNT｜Tyndale House's gloss｜Tyndale House's extended Strong's numbers｜morphology〉
