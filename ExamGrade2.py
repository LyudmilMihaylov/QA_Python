mark = int(input("Enter the exam mark (1-100): "))
level = int(input("Enter the student level (1 or 2): "))

if mark < 1 or mark > 100:
    print("Error: Marks must be between 1 and 100")
elif level == 1:
    if mark < 50:
        print("Fail")
    elif 50 <= mark <= 60:
        print("Pass")
    elif 61 <= mark <= 70:
        print("Merit")
    else:
        print("Distinction")
elif level == 2:
    if mark < 40:
        print("Fail")
    elif 40 <= mark <= 50:
        print("Pass")
    elif 51 <= mark <= 65:
        print("Merit")
    else:
        print("Distinction")
else:
    print("Error: Invalid level")