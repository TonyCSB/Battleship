# c5e14_file_words.py
# Tony Chen

def main():
    print("This program counts the number of lines, words and")
    print("characters in a file.\n")

    infileName = input("The file's name: ")
    
    infile = open(infileName, "r")

    lines = 0
    words = 0
    characters = 0

    for l in infile:
        lines = lines + 1

        for w in l.split():
            words = words + 1
            characters = characters + 1

            for ch in w:
                characters = characters + 1

    infile.close()

    print("Lines:      {0:>5}".format(lines))
    print("Words:      {0:>5}".format(words))
    print("Characters: {0:>5}".format(characters))
    
main()
