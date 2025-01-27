def determine_grade(marks):
    if marks>=90:
        return "A"
    elif marks>=80:
        return "B"
    elif marks>=70:
        return "C"
    elif marks>=60:
        return "D"
    elif marks>=50:
        return "E"
    else:
        return "F"
    try:
        marks = int(input("Enterthe marks obtained(out of 100):"))
        if 0<= marks <= 100:
            grade = determine_grade(marks)
            print(f"The grade for {marks} marks is: {grade}")
            else:
                print("Invalid input."
                      expect ValueError:
                      print("Invalid input.")

