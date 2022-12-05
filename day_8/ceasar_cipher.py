from art import logo


print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    text = [i for i in text]

    for i in range(len(text)):
        idx = alphabet.index(text[i])
        if idx+shift < len(alphabet):
            text[i] = alphabet[idx+shift]
        else:
            text[i] = alphabet[len(alphabet) - (idx+shift)]

    return "".join(text)

def decrypt(text, shift):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    text = [i for i in text]

    for i in range(len(text)):
        idx = alphabet.index(text[i])
        text[i] = alphabet[(idx-shift)]

    return "".join(text)

if direction == "encode":
    print(encrypt(text, shift))
else:
    print(decrypt(text, shift))

