# c5e4_acronym.py
# David Owen

def main():
    print("This program inputs a phrase, and outputs an acronym")
    print("representing that phrase.\n")
    
    phrase = input("Phrase? ")

    words = phrase.split()

    acronym = ""

    for words in words:
        acronym = acronym + words[0]

    print("\nAcronym:", acronym.upper())

main()
