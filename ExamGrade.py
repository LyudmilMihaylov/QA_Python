mark = int(input("Enter the exam mark (1-100): "))

if mark < 1 or mark > 100:
    print("Error: Marks must be between 1 and 100")
elif mark < 50:
    print("Fail")
elif 50 <= mark <= 60:
    print("Pass")
elif 61 <= mark <= 70:
    print("Merit")
else:
    print("Distinction")