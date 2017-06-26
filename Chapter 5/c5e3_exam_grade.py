# c5e3_exam_grade.py
# Tony Chen

def main():
    score = input("Enter the exam score: ")

    print()

    gradeStr = "F" * 6 + "D" + "C" + "B" + "A" * 2

    score2 = int(int(float(score)) / 10)

    grade = gradeStr[score2]

    print("The grade of {0} is {1}.".format(score, grade))

main()
