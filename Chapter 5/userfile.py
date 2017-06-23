# userfile.py
# John Zelle

from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksavefilename

def main():
    print("This program creates a file of usernames from a")
    print("file of names.")

    # get the file names
    infileName = askopenfilename()
    outfileName = asksavefilename()

    # open the files
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    # process each line of the input file
    for line in infile:
        # get the first and last names from line
        first, last = line.split()
        # create the username
        uname = (first[0] + last[:7]).lower()
        # write it to the output file
        print(uname, file = outfile)

    # close both files
    infile.close()
    outfile.close()

    print("Usernames have be written to", outfileName)

main()
