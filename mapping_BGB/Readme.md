File processed for mapping Berean Greek Bible and its associated data (first imported on 20Aug2018).

Berean Greek Bible is copyrighted and licensed by Bible Hub.  Used with permission.

© 2016 by Bible Hub. The Holy Bible, Berean Bible. All Rights Reserved Worldwide. Free Licensing for use in Websites, Apps, Software, and Audio:  <a href='http://berean.bible/licensing.htm'>http://berean.bible/licensing.htm</a>

Special thanks to John Isett, Bible Hub, for all his help and support.

<hr>

Berean Greek Bible and its associated data (inclusive) were taken into review and processed, for compilation of a NA-equivalent Greek New Testament.

The compilation process is briefly described below:

- Original variant markers in Berean database (inclusive) were reviewed, a few of them were refined. A few missing variants from Byzantine text were added to the database.  The were marked with "＋BYZ" in <a href='https://github.com/eliranwong/OpenGNT/blob/master/mapping_BGB/berean_tablesInclusive.csv.zip'>the database</a>, formatted for compilation.
- BGB was compared with <a href='https://github.com/greekcntr/BHP'>Bunning Heuristic Prototype Greek New Testament</a>, BHP in short, released by <a href='https://greekcntr.org'>Center for New Testament Restoration</a>.  The comparison considers major variants only, ignoring minor issues like movable ν, αλλ vs αλλα, etc.  BHP was taken into weighing textual decisions, as it is one of the latest projects, reflecting the best and earliest manuscripts.  The review results in adaptation of some BHP's readings in place of some BGB readings.  They were marked with "＋BHP" in <a href='https://github.com/eliranwong/OpenGNT/blob/master/mapping_BGB/berean_tablesInclusive.csv.zip'>the database</a>, formatted for compilation.  <i>Remarks:</i> BHP was not available for consideration in the original development of Berean Greek Bible, because it had not been published at the first launch of Berean Greek Bible.
- All TR, BYZ, WH, NE variants, originally marked in Berean database with symbols "{} ⧼⧽ () 〈〉", and some of SBL variants, marked with "〈〉", were taken away from the compilation.
- Verses containing ⇔ in original Berean database were reviewed and compared with free GNT editons (i.e. TR, BYZ, WH, SBL, BHP).  Word order in 71 verses were adapted from other editions and were documented <a href='https://github.com/eliranwong/OpenGNT/blob/master/mapping_BGB/compare_OGNT_BGB/wordOrder_BGB_OGNT.tsv'>HERE</a>.
- Berean Greek Bible uses KJV versification.  Original GNT's versification (Nestle 1904) had been worked out, with minor variations following SBLGNT's versification.
- Punctuation marks were taken away during the compilation.

<hr>

<b>Result:</b> A NA-Equivalent text, <a href='https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT_BASE_TEXT.zip'>OGNT (version 3)</a>, compiled from Berean Greek data (Inclusive)

<a href='https://github.com/eliranwong/OpenGNT/tree/master/mapping_BGB/compare_OGNT_BGB'>Compare OGNT (version 3) with original BGB</a>

<a href='https://github.com/eliranwong/OpenGNT/tree/master/mapping_BGB/compare_OGNT_NA28'>Compare OGNT (version 3) with NA28</a>
