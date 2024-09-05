import random

def choose_word():
    words = ["python", "hangman", "challenge", "programming", "developer"]
    return random.choice(words)

def display_hangman(tries):
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        """,
        """
           ------
           |    |
           |
           |
           |
           |
        """,
        """
           ------
           |
           |
           |
           |
           |
        """
    ]
    return stages[tries]

def play_hangman():
    word = choose_word()
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Welcome to Hangman!")

    while not guessed and tries > 0:
        print(display_hangman(tries))
        print("Word: ", " ".join([letter if letter in guessed_letters else "_" for letter in word]))
        print("\nGuessed letters: ", " ".join(guessed_letters))
        guess = input("Please guess a letter or word: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess not in word:
                print("Wrong guess.")
                guessed_letters.append(guess)
                tries -= 1
            else:
                print("Good guess!")
                guessed_letters.append(guess)
                if all(letter in guessed_letters for letter in word):
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed that word.")
            elif guess != word:
                print("Wrong word.")
                guessed_words.append(guess)
                tries -= 1
            else:
                guessed = True
        else:
            print("Invalid input. Please try again.")

    if guessed:
        print(f"Congratulations! You've guessed the word: {word}")
    else:
        print(display_hangman(tries))
        print(f"Sorry, you've run out of tries. The word was: {word}")

play_hangman()
