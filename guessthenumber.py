import random

print('Hello. What is your name?')
name = input()


print('Well, ' + name + ' , I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 3):
    print('Take a guess.')
    guess = int(input())

    
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your gess is too high.')
    else:
        break

if guess == secretNumber:
    print('Good Job, ' + name + ' ! You Guessed my number in ' + str(guessesTaken) + ' guesses.')
else:
    print('Nope. The number i was thinking of was'  +  str(secretNumber))
          
print('You took ' + str(guessesTaken) + ' guesses.')
