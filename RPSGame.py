import random

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

def play_game():
    user_wins = 0
    computer_wins = 0
    rounds = 0

    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        print(f"Computer chose: {computer_choice}")
        
        result = get_winner(user_choice, computer_choice)
        rounds += 1
        
        if result == "user":
            print("You win!")
            user_wins += 1
        elif result == "computer":
            print("Computer wins!")
            computer_wins += 1
        else:
            print("It's a draw!")
        
        print(f"Rounds: {rounds}, Your wins: {user_wins}, Computer wins: {computer_wins}")
        
        if input("Play again? (yes/no): ").lower() != 'yes':
            break

    print("Thanks for playing!")

play_game()
