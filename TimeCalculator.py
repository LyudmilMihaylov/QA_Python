while True:
    print("1. Add Times")
    print("2. Subtract Times")
    print("9. Exit")
    
    choice = input("Select an option: ")

    if choice == '9':
        break
    elif choice in ['1', '2']:
        time1 = input("Enter the first time (DD:HH:MM): ")
        time2 = input("Enter the second time (DD:HH:MM): ")

        days1, hours1, minutes1 = map(int, time1.split(":"))
        days2, hours2, minutes2 = map(int, time2.split(":"))

        if choice == '1':
            # Perform time addition
            total_days = days1 + days2
            total_hours = hours1 + hours2
            total_minutes = minutes1 + minutes2

            if total_minutes >= 60:
                total_hours += total_minutes // 60
                total_minutes %= 60

            if total_hours >= 24:
                total_days += total_hours // 24
                total_hours %= 24

        elif choice == '2':
            # Perform time subtraction
            total_days = days1 - days2
            total_hours = hours1 - hours2
            total_minutes = minutes1 - minutes2

            if total_minutes < 0:
                total_minutes += 60
                total_hours -= 1

            if total_hours < 0:
                total_hours += 24
                total_days -= 1

        print(f"Result: {total_days:02}:{total_hours:02}:{total_minutes:02}")
    else:
        print("Invalid option, please try again.")