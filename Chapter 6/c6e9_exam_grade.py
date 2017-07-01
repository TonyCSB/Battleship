# c6e9_exam_grade.py
# Tony Chen

def grade(score):
    gradeStr = "F" * 6 + "D" + "C" + "B" + "A" * 2
    score = int(int(score) / 10)
    grade = gradeStr[score]
    return grade

def main():
    print("This program returns the letter grade for a score.\n")

    score = float(input("Enter the exam score: "))

    gradeResult = grade(score)

    print()

    print("The grade of {0:0.0f} is {1}.".format(score, gradeResult))

main()
