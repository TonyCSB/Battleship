# c5e10_word_length.py
# David Owen

def main():
    print("This program inputs a sentence and outputs the average")
    print("length of the words in the sentence.\n")

    sentence = input("Sentence? ")
    words = sentence.split()
    total = 0

    for word in words:
        for c in word.lower():
            if c >= "a":
                if c <= "z":
                    total = total + 1

    print("\nAverage word length:", total / len(words))

main()
