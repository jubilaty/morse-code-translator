MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

REVERSE_MORSE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def encoder(text):
    morse = []
    for char in text.upper():
        morse.append(MORSE_CODE_DICT.get(char, '?'))
    return ' '.join(morse)

def validate_morse(morse):
    codes = morse.split()
    valid_codes = REVERSE_MORSE_DICT.keys()
    return all(code in valid_codes for code in codes)

def decoder(morse):
    if not validate_morse(morse):
        print("Warning: some Morse code is invalid (shown as '?')")
    text = []
    for code in morse.split():
        text.append(REVERSE_MORSE_DICT.get(code, '?'))
    return ''.join(text)

def main():
    print("\nMorse Code Translator")
    while True:
        print("Options:")
        print("1. Encode text -> Morse")
        print("2. Decode Morse -> text")
        print("3. Validate Morse code")
        print("4. Exit")
        choice = input("Choose (1/2/3/4): ").strip()

        if choice == "1":
            text = input("Enter text: ")
            print(f"Morse: {encoder(text)}")
        elif choice == "2":
            morse = input("Enter Morse: ")
            print(f"Text: {decoder(morse)}")
        elif choice == "3":
            morse = input("Enter Morse code to validate: ")
            if validate_morse(morse):
                print("Valid Morse code")
            else:
                print("Invalid Morse code")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
