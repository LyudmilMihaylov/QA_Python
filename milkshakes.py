def main():
    # Milkshake options and prices
    milkshakes = {
        "Vanilla": 3.50,
        "Chocolate": 4.00,
        "Strawberry": 3.75
    }

    budget = float(input("Enter your budget: $"))

    while True:
        print("\nAvailable Milkshakes:")
        for flavor, price in milkshakes.items():
            print(f"{flavor} - ${price:.2f}")
        print("Q. Quit")

        choice = input("Select a milkshake by flavor or 'Q' to quit: ").capitalize()

        if choice == 'Q':
            print("Goodbye!")
            break

        if choice in milkshakes:
            price = milkshakes[choice]
            if price > budget:
                print("You can't afford that.")
            else:
                budget -= price
                print(f"You ordered {choice}. Remaining budget: ${budget:.2f}")
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()