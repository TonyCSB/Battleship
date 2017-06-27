# c5e7_cipher.py
# Tony Chen

def main():
    print("This program can be used to encode (or decode) a")
    print("message using a simple Caesar cipher (each letter")
    print("shifted by a fixed amount).\n")

    text = input("Message? ")

    key = int(input("How far should each letter by shifted? "))

    print()

    messageList = []

    for ch in text:
        messageList.append(chr(ord(ch) + key))

    message = "".join(messageList)

    print("Result:", message)

main()
