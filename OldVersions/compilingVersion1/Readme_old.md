# Main Source - TANTT:

The text of OpenGNT [OGNT] is largely built on a scholarly database, "TANTT - Tyndale Amalgamated NT Tagged texts", dated on 6th June 2018.
<br><br>
TANTT is "created and curated collaboratively by Tyndale scholars, directed by David Instone-Brewer with the oversight of Peter Williams, and by their successors."  It is freely distributed at <a href='https://github.com/tyndale/STEPBible-Data' target='_blank'>https://github.com/tyndale/STEPBible-Data</a>, under a creative license, namely <a href='https://creativecommons.org/licenses/by-nd/4.0/legalcode' target='_blank'>CC BY-NC-ND 4.0 with additional specified relaxations</a>.
<br><br>
Below is the official introduction of TANTT:
<br><br>
"Greek text created from the SBLGNT+apparatus, following the decisions made by NA27, listing the major editions that also use that form (SBL, Treg, TR, Byz, WH, NA28). Variants are being added from major editions plus the 1st 4 centuries of MSS (from Bunning). All words are tagged lexically (extended Strong linked to LSJ) and morphologically (Robinson based on Tauber plus a few missing details) plus context-sensitive meanings for words with more than one meaning. An independant scholar checked the result against NA27 and pointed out a few differences which were fixed (see <a href='https://github.com/tyndale/STEPBible-Data/issues?q=is%3Aissue+is%3Aclosed' target='_blank'>the issues in github</a>)."
<br><br>
David Instone-Brewer's words about the source of TANTT:<br>
"It comes from:<br>
• SBLGNT text<br>
• SBLGNT variants marked as NIV (ie NA+NIV)<br>
• places where this variant meant NIV in distinction to NA were weeded out, leaving NA variants<br>
• these were incorporated into the SBLGNT text to produce the equivalent NA text<br>
• a few errors in this process were sent as corrections to Github (where they are recorded)<br>
So the source is SBLGNT + intelligent manpower.<br>
The source is not the Bible Society text."<br>
[quoted from a social media group on 19JULY2018]
<br><br>
TANTT is, therefore, developed from <a href='sblgnt.com' target='_blank'>SBLGNT and its apparatus</a>.  Additional work had been done by Tyndale House's scholars to map James Tauber's morphology and Tyndale House's extended Strong's numbers.  Variant markers added for each word to indicate major differences of variants among eight modern editions of Greek New Testament.  Eliran Wong contributed to the final shape of TANTT data, through <a href='https://github.com/tyndale/STEPBible-Data/issues?q=is%3Aissue+is%3Aclosed' target='_blank'>interactions with David Instone-Brewer</a>.  In short, at the time of OGNT being finalised, the main text of TANTT is the closest equivalent to the text of NA27, keyed to Tyndale House's extended Strong's numbers and James Tauber's morphology, and variants from major modern Greek New Testament Editions.
<br><br>
<b>Credits of TANTT data:</b>
<br><br>
"Tyndale House, Cambridge" [<a href='www.TyndaleHouse.com' target='_blank'>www.TyndaleHouse.com</a>],<br>
and "STEP Bible" [<a href='www.STEPBible.org' target='_blank'>www.STEPBible.org</a>]<br>
and source at <a href='tyndale.github.io/STEPBible-Data/' target='_blank'>tyndale.github.io/STEPBible-Data/</a>

# Develop OGNT from TANTT

OpenGNT project bases on TANTT database as major materials and takes that further to develop an eclectic Greek text, <a href='https://github.com/eliranwong/OpenGNT/tree/master/CompareOGNTwithNA28' target='_blank'><b>equivalent to the text of NA28</b></a>, and <a href='https://github.com/eliranwong/OpenGNT#enhancement--forthcoming-additions' target='_blank'>other add-on enhancements</a>.  All variants in origianl TANTT database, marked with "N" or "M" are reviwed.  Additional variant entries are added and word order are aligned with the latest editions of Alexandrian text-type.  All works done in OpenGNT project are additions rather than derivatives.  Where original TANTT data are not clear, precise or accurate enough, original TANTT data are not changed, in accordance to the license requirement of TANTT.  Whenever new entries on variants are added in OGNT database, original TANTT data are all kept for in place for comparison with corresponding new entries [For details, read <a href='https://github.com/eliranwong/OpenGNT/blob/master/From_TANTT_to_OpenGNT/005-009.csv.zip' target='_blank'>files 005-009...csv HERE</a>].
<br><br>
This results in that OpenGNT database distinguish better between variants of NA27 and NA28 than original TANTT database.  Original TANTT database has potential to produce an eclectic Greek text, eqiuvalent to the text of NA27.  OGNT offers an extra possiblity to compile an eclectic Greek text, <a href='https://github.com/eliranwong/OpenGNT/tree/master/CompareOGNTwithNA28'><b>equivalent to the text of NA28</b></a>.  Indeed, an eclectic Greek text had been produced in OpenGNT project, namely OGNT, which is totally based on open-materials mentioned above.  The text of OGNT is now currently <a href='https://github.com/eliranwong/OpenGNT/tree/master/CompareOGNTwithNA28'><b>the closest equivalent to the text of NA28</b></a>, offerring a free Greek New Testament for biblical studies or creative researches.
<br><br>
<a href='https://github.com/eliranwong/OpenGNT#enhancement--forthcoming-additions'>Additional content</a> is worked out by Eliran Wong who are responsible for all the errors, if any.  You are more than welcomed to report errors at <a href='https://biblebento.com/contact/contactform.php' target='_blank'>https://biblebento.com/contact/contactform.php</a>

# Files in this directory

Major developement of OGNT can be found from 005...csv to 009...csv.<br>
Information is available at the top of each file for major additions to the original database.<br>
<br>
- 005...-007...csv are major files developed further from the database of TANTT.  Around a thousand of variants had been reviewed one by one.  New alternate entries for hundreds of variants had been added.  New alternate entries include information, like missing variants from original TANTT database, tagging information, morphology, and variant markers.  Original TANTT data are not changed.  New Entries does not replace TANTT data.  Instead, they are placed above each of the corresponding entries of original TANTT data.  This aims to provide an easy way for users to compare all alternate entries with original TANTT data.<br>
- 008...csv have all words finalised for the base text of OGNT project.  All words are keyed to James Tauber's morphology and Tyndale House's extended Strong's numbers.  Word orders are aligned with NA28 for comparison.  All additions developed in 005...-007...csv had been integrated in this file.<br>
- In 009...csv Additional 181 Greek variants had been reviewed, with new variant markers added as new alternate entries.  <b>This file is used as the main database for the rest of Open Greek New Testament Project</b>.<br>
- <a href='https://github.com/eliranwong/OpenGNT#enhancement--forthcoming-additions'>All future additions or corrections</a> will be integrated in the file "<a href='https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT.csv.zip'>010_OGNT.csv</a>" directly.

# Differences between OGNT and TANTT

- At the time of the text of OGNT being finalised, <a href='https://github.com/eliranwong/OpenGNT/tree/master/CompareOGNTwithNA28'><b>OGNT is the closest equivalent to the text of NA28</b></a> whereas TANTT is the closest equivalent to the text of NA27.<br><br>
- OGNT has hundreds of additional alterate readings on hundreds of Greek words.<br>
<br>
- OGNT covers more variants than TANTT in many places.<br>
For example, in Titus 1:5, the word in the main text is "ἀπέλιπόν":<br>
OGNT database lists two variants for it, i.e. BR=κατελιπον, WH=απελειπον<br>
However, original TANTT list one variant only, i.e. WH=απελειπον<br>
<br>
- OGNT has some Greek variants, which are missing in original TANTT database.<br>
For example, OGNT include the following ECM variants, which are missing in TANTT database.<br>
καὶ in James 2:4<br>
ὦσιν in James 2:15<br>
τοῦ in James 4:10<br>
οὐχ in 2Peter 3:10<br>
ταῖς in 2Peter 3:16<br>
<br>
- OGNT's alternate readings often provide more precise, if not more accurate, readings.<br>
For example, in Mark 13:24:<br>
OGNT's analysis: 〔BMR｜αλλ｜Ἀλλ᾿｜G235｜CONJ｜ἀλλά｜but〕INSTWH=αλλα<br>
TANTT's analysis: 〔BINRSTWH｜αλλα｜Ἀλλὰ｜G235｜CONJ｜ἀλλά｜but〕<br>
<br>
Another example, in Col 2:16:
OGNT's analysis: 〔INTW｜νεομηνιας｜νεομηνίας｜G3561｜N-GSF｜νουμηνία｜New Moon〕BRSH=νουμηνιας<br>
TANTT's analysis: 〔BINRSTWH｜νουμηνιας｜νουμηνίας｜G3561｜N-GSF｜νουμηνία｜New Moon〕<br>
<br>
- OGNT's alternate readings provide Strong's numbers, morphology information and variants markers for Greek variants, which are not available in the original TANTT database.<br>
For example, in 2Peter 2:15,<br>
OGNT's analysis: 〔BMRST｜... καταλιπόντες ... V-2AAP-NPM ... INWH＝καταλειποντες<br>
TANTT's analysis: 〔ImNWH｜... καταλείποντες ... V-PAP-NPM ... BMRST=καταλιποντες<br>
<br>
- Each alternate reading of OGNT have one Strong's number only, rather than multiple Strong's numbers for a single entry as in some of TANTT data.  This facilitates developing modules for bible applications / softwares.<br>
<br>
- In addition, OGNT expands the original TANTT database with <a href='https://github.com/eliranwong/OpenGNT#enhancement--forthcoming-additions' target='_blank'>many useful features</a>.
