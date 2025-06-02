import re
from phonemizer import phonemize
from phonemizer.backend.espeak.espeak import EspeakBackend
import subprocess

# Load Latin script from file
def load_text(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

# Convert text to IPA using phonemizer.
def text_to_ipa(text):
    try:
        # Construct the command - can you tell I'm a Windows user?
        cmd = ['espeak-ng', '-q', '--ipa=3', text]

        # Ensure UTF-8 is being used so the script doesn't shit itself over the fact Futhorc is being used for the first time in a millenia
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, # AAAAAA
            encoding='utf-8'
        )

        # Handle output
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            raise RuntimeError(result.stderr.strip())
    except FileNotFoundError:
        raise RuntimeError("espeak-ng is not installed or not in PATH")
    ipa = phonemize(
        text,
        language='en-gb',
        backend='espeak',
        strip=True,
        preserve_punctuation=True,
        njobs=1
    )
    return ipa

# IPA -> Futhorc rune mapping
# To do this, we need to make an SSBE phoneme inventory.
# This aims to approximate Futhorc to Standard Southern British English's phoneme inventory.
# Functionally, this is a spelling reform like Deseret.
ipa_to_futhorc = {
    # Vowels
    'æ': 'ᚫ', 'a': 'ᚪ', 'ɑ': 'ᚪ',
    'e': 'ᛖ', 'ɛ': 'ᛖ',
    'i': 'ᛁ', 'ɪ': 'ᛁ',
    'o': 'ᚩ', 'ɔ': 'ᚩ', 'ɒ': 'ᚩ',
    'u': 'ᚢ', 'ʌ': 'ᚢ', 'ɐ': 'ᚢ', # [ɐ] is not traditionally included but exists.
    'ʊ': 'ᛟ', 'uː': 'ᛟ', # "oo"
    'ə': 'ᛖ', 'ɜ': 'ᛖ', # This feels good for schwa but it's a work in progress. 

    # Diphthongs and vowel pairs
    'aɪ': 'ᛇ', 'a‍ʊ': 'ᚪᚹ',
    'eɪ': 'ᛖᛁ', 'əʊ': 'ᚩᚢ', 'ɔɪ': 'ᚩᛁ',

    # Consonants
    'θ': 'ᚦ', 'ð': 'ᚦ',
    'b': 'ᛒ',
    'p': 'ᛈ',
    't': 'ᛏ',
    'd': 'ᛞ',
    'k': 'ᚳ',
    'g': 'ᚷ', 'ɡ': 'ᚷ',
    'dʒ': 'ᛞᛄ',  # Like DG in, say, "wedge". 
    'f': 'ᚠᚠ', 'v': 'ᚠ', # Welsh system: one ᚠ for V, ᚠᚠ for F. 
    's': 'ᛋ', 'z': 'ᛋ', # TESTME: Should this also have a Welsh system or is that a bit evil?
    'tʃ': 'ᚳᚻ', # We are making the SH/CH the same as standard spelling. 
    'ʃ': 'ᛋᚻ',
    'ʒ': 'ᛄ', # TESTME: Do we want a ᚻ here? Think "vision". 
    'h': 'ᚻ',
    'm': 'ᛗ',
    'n': 'ᚾ',
    'ŋ': 'ᛝ',
    'l': 'ᛚ', 'r': 'ᚱ',
    'j': 'ᛄ',
    'w': 'ᚹ',
    'ɹ': 'ᚱ', 'r': 'ᚱ', # Accounting for any RPist weirdness, they hate the bunched r for some reason

    # Glottal stop
    # You can approximate this with ᛁ
    # For now, I am doing so using ᛠ, which is currently unused.
    'ʔ': 'ᛠ',

    # IPA markers we don't want
    'ː': '', # Long consonants
    'ˈ': '', 'ˌ': '', # Stress markers
    '\u200d': '', # Invisible weirdness????? what do u want sis

    # General American edge-cases
    # This doesn't account for differences to SSBE above.
    #   'oʊ': 'ᛟ', # Very important - if you're an American, you'll need to re-account for ᛟ in its entirety.
    #   'ɜɹ': 'ᛖᚱ',
}

# Convert IPA to runes
def ipa_to_runes(ipa_text):
    # Sort keys so longer IPA symbols like 'tʃ' get replaced first
    symbols_sorted = sorted(ipa_to_futhorc.keys(), key=lambda x: -len(x))
    rune_text = ipa_text
    for symbol in symbols_sorted:
        rune = ipa_to_futhorc[symbol]
        rune_text = rune_text.replace(symbol, rune)
    return rune_text

# Add runic word spacing
def add_runic_spacing(text):
    return re.sub(r'\s+', ' ᛫ ', text.strip())

# Save runes to output file
def save_runes(output, filename='output_runes.txt'):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(output)

# Main execution
def main():
    input_text = load_text('input_latin.txt')
    ipa = text_to_ipa(input_text)
    print("IPA Output:\n", ipa)

    runes = ipa_to_runes(ipa)
    runes_with_spacing = add_runic_spacing(runes)
    
    print("\nFuthorc Output:\n", runes_with_spacing)
    save_runes(runes_with_spacing)

if __name__ == '__main__':
    main()

