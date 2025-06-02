Fuþorcettanere
====

This is an experimental script for converting a text from the Latin alphabet to Old Saxon Futhorc (also known as Runic, Runick, Futhark, runes, and a bunch of other stuff). I am doing this with the intent to produce works in the script. However, it is not merely done with the intent to replace text, but phonetically approximate using Futhorc as it was originally used by the Anglo-Saxons. I took inspiration from the [Deseret Classics](https://www.deseretalphabet.info/classics/) series of books, which used LuaText to transliterate English into Deseret. All transcriptions are based on British English as exists in Phonemizer.

The name "Fuþorcettanere" means Futhorciser.

Variations
====
* `main_trad_spacing.py` - Outputs Futhorc with the traditional, accurate spacing, using large dots, eg. ᛏᛖ ᛫ ᛋᚻᛖᛚᚩᚳ ᛫ ᚻᛖᛟᛗᛋ ᛫ ᛋᚻᛁ ᛫ ᛁᛋ ᛫ ᚩᛚᚹᛖᛁᛋ ᛫ ᚦᛖ ᛫ ᚹᛟᛗᛖᚾ 
* [WIP] `main_modern_punc.py` - Outputs Futhorc with the punctuation of the original text.

Notes for Compatibility
====

This outputs Futhorc in Unicode UTF-8 encoding. If you're from an English-speaking country you should have the extension natively, but if you don't, or use a very minimalist font, you may see a bunch of squares. In my experience fixing this is an actual nightmare (try to find expanded Zhuyin or Chu Nom fonts and come back) but you should be fine after a couple of pints. 

I produced this using [Phonemizer](https://pypi.org/project/phonemizer/), a wonderful extension that converts text into phonemes. Without this, it would have been extremely difficult to produce. 

You'll need to install [eSpeak-NG](https://github.com/espeak-ng/espeak-ng) to get Phonemizer off the ground. You will need to include it in PATH, but I've included a ridiculous subprocess to make sure the program WILL find espeak once it's all squared away, so hopefully that'll solve any problems you have. 

To-do
====
* Produce option to output Futhorc with the punctuation with the original text
* De-Futhorcettanere option
* Don't use the fucking kernel lmao
* Make the code good
* Find a GNU font for Futhorc? Make one? Then include it in the repo.
* American English support

Disclaimer
====
The intent of this script is to promote Old Saxon Futhorc usage. However, I do not endorse, encourage, or condone usage of the runes for any movements associated with racism, white supremacy/nationalism/identitarian/"pride"/etc, and so on, you know the drill. I prefer encouraging use of the script as just that: A script. If you're one of those weird kooks who want to use it, well, I can't stop you, just know I'll be giving you the angry teacher stare. 

References
====
If you want, you can also see [references.bib](/references.bib).
* Bernard, M. & Titeux, H. 2021. 'Phonemizer: Text to Phones Transcription for Multiple Languages in Python' in Journal of Open Source Software (6)68, pp. 3958. The Open Journal. https://doi.org/10.21105/joss.03958. 
* Halsall, M. 1981. The Old English Rune poem: a critical edition. University of Toronto Press. ISBN: 978-0-8020-5477-7

Licence
====
As a supporter of the [Free Software Movement](https://www.fsf.org/about/) and its values, this is published under a [GNU General Public Licence v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html). Contributions are encouraged. 


