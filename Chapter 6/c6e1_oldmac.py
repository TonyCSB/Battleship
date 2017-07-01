# c6e1_oldmac.py
# Tony Chen

def startEnd():
    return "Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!\n"

def middle(animal, sound):
    return ("And on that farm he had a " + animal + ", Ee-igh, Ee-igh, Oh!\n" +
           "With a " + sound + ", " + sound + " here and a " + sound +
           ", " + sound + " there.\n" + "Here a " + sound + ", there a " +
           sound + ", everyewhere a " + sound + ", " + sound + ".\n")

def main():
    animal = ["cow", "pig", "horse", "chicken", "duck"]
    sound = ["moo", "snort", "neigh", "cluck", "quack"]
    for i in range(5):
        s = startEnd()
        m = middle(animal[i], sound[i])
        e = startEnd()
        print(s + m + e)

main()
