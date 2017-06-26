# c5e9_sentence_words.py
# Tony Chen

def main():
    print("This program counts the number of words")
    print("in a sentence entered by the user.\n")

    sentence = input("Please enter the sentence: ")

    count = 0

    for ch in sentence.split():
        count = count + 1

    print()

    print("The number of words is", count)
    
main()
