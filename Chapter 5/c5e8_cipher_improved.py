# c5e8_cipher_improved.py
# Tony Chen

def main():
    print("This program can be used to encode (or decode) a")
    print("message using a simple Caesar cipher (each letter")
    print("shifted by a fixed amount).\n")

    text = input("Message? ")

    key = int(input("How far should each letter by shifted? "))

    print()

    messageList = []

    characterList = []

    for i in range(65, 91):
        characterList.append(chr(i))

    characterList.append(" ")

    for i in range(97, 123):
        characterList.append(chr(i))

    character = "".join(characterList + characterList)

    for ch in text:
        messageList.append(character[character.find(ch) + key])

    message = "".join(messageList)

    print("Result:", message)

main()
