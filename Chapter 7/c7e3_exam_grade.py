# c7e3_exam_grade.py
# Tony Chen

def main():
    print("This problem accepts an exam score as input")
    print("and calculate the corresponding grade.\n")
    
    try:
        score = int(input("Score? "))
        if score <= 100:
            if score >= 90:
                grade = "A"
            elif score >= 80:
                grade = "B"
            elif score >= 70:
                grade = "C"
            elif score >= 60:
                grade = "D"
            elif score >= 0:
                grade = "F"
            else:
                print("\nPlease enter a positive value.")
        else:
            print("\nPlease enter a number less than or equal to 100.")

        print("\nThe grade is", grade)

    except UnboundLocalError:
        pass

    except:
        print("\nPlease enter a normal value.")

main()
