
#the character dictionary for encode/dec obv
char_dict = {
    ' ': '(', '!': ')', '"': '*', '#': '+', '$': ',', '%': '-', '&': '.', "'": '/',
    '(': '0', ')': '1', '*': '2', '+': '3', ',': '4', '-': '5', '.': '6', '/': '7',
    '0': '8', '1': '9', '2': ':', '3': ';', '4': '<', '5': '=', '6': '>', '7': '?',
    '8': '@', '9': 'A', ':': 'B', ';': 'C', '<': 'D', '=': 'E', '>': 'F', '?': 'G',
    '@': 'H', 'A': 'I', 'B': 'J', 'C': 'K', 'D': 'L', 'E': 'M', 'F': 'N', 'G': 'O',
    'H': 'P', 'I': 'Q', 'J': 'R', 'K': 'S', 'L': 'T', 'M': 'U', 'N': 'V', 'O': 'W',
    'P': 'X', 'Q': 'Y', 'R': 'Z', 'S': '[', 'T': '\\', 'U': ']', 'V': '^', 'W': '_',
    'X': '`', 'Y': 'a', 'Z': 'b', '[': 'c', '\\': 'd', ']': 'e', '^': 'f', '_': 'g',
    '`': 'h', 'a': 'i', 'b': 'j', 'c': 'k', 'd': 'l', 'e': 'm', 'f': 'n', 'g': 'o',
    'h': 'p', 'i': 'q', 'j': 'r', 'k': 's', 'l': 't', 'm': 'u', 'n': 'v', 'o': 'w',
    'p': 'x', 'q': 'y', 'r': 'z', 's': '{', 't': '|', 'u': '}', 'v': '~', 'w': ' ',
    'x': '!', 'y': '"', 'z': '#', '{': '$', '|': '%', '}': '&', '~': "'", '\t': '§'
}
def main():
    print("This is a encoder/decoder.")
    while True:
        try:
            answerone = int(input("Press 1 for encoder, Press 2 for decoder:\n"))
            if answerone == 1:
                encodedmessage = encoder()
                print("")
                break
            elif answerone == 2:
                decodedmessage = decoder()
                print("")
                break
            else:
                pass
        except ValueError:
            pass

def encoder():
    #asks what should be encoded, then look through every character and change it to the other character in the key.
    x = input("What message would you like to be encoded?\n")
    for y in x:
        try:
            character = char_dict[y]
            print(character, end="")
        except KeyError:
            print(y, end="")

def decoder():
    #Loops for character in the dict, if not there just print
    x = input("What message would you like to be decoded?\n")
    for y in x:
        for original_char, encoded_char in char_dict.items():
            if encoded_char == y:
                print(original_char, end="")
                break
        else:
            print(y, end="")


if __name__ == "__main__":
    main()
