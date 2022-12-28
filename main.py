from logo import logo

# Morse code chart
MORSE_CODE = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
              "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.",
              "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
              "y": "-.--", "z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
              "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----", ",": "--..--",
              ".": ".-.-.-", "?": "..--..", "/": "-..-.", "-": '-....-', "(": "-.--.", ")": "-.--.-", ":": "---...",
              ";": "-.-.-.", "&": ".-...", "=": "-...-", "+": ".-.-.", "_": "..--.-", '"': ".-..-.", "$": "...-..-",
              "@": ".--.-.", "'": ".---.", "!": "-.-.--"}


# Encrypt a string to Morse Code
def encode(string):
    """Takes a plain text and returns a morse code encoded text"""
    encoded_text = ""

    for char in string:
        if char in MORSE_CODE:
            encoded_text += (MORSE_CODE[char]) + " "
        else:
            encoded_text += char

    return encoded_text


# Decode a morse code encrypted text
def decode(string):
    """Takes a morse code and returns the decrypted message"""
    # Get a list keys from morse chart
    key_list = list(MORSE_CODE.keys())

    # Get a list values from morse chart
    val_list = list(MORSE_CODE.values())

    decoded_text = ""
    for char in string.split(" "):

        if char in val_list:
            # Get the key of a value
            position = val_list.index(char)
            decoded_text += key_list[position]

        elif char == "":
            decoded_text += " "

        else:
            decoded_text += char

    return decoded_text


run_converter = True

while run_converter:
    print(logo)
    # Receive input from user and carry out the chosen function
    function_choice = input("Do you want to encrypt or decrypt a text? (Type encode or decode):\n")

    if function_choice == "encode":
        text = input("Enter a text to encrypt into Morse code:\n").lower()
        print(f"Your text converted into morse code: {encode(text).capitalize()}")
    elif function_choice == "decode":
        text = input("Enter a morse code encrypted text to decrypt:\n").lower()
        print(f"Your morse converted into a text: {decode(text).capitalize()}")
    else:
        print("Invalid Input! Please select whether you want to encrypt or decrypt a text.")

    keep_running = input("Would you like to continue encoding and decoding texts? (Type yes or no):\n").lower()

    # Stops the Converter from running
    if keep_running == "no":
        run_converter = False
