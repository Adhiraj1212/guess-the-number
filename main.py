from art import *
import random
import os
def guess_the_number():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to the Number Guessing Game!")
    print(art)
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if (difficulty == "easy"):
        attempts = 10
    elif (difficulty == "hard"):
        attempts = 5
    else:
        print("Invalid input. Please try again.")
        return
    number = random.randint(1, 100)
    while attempts > 0:
        print(f"You have {attempts} attempts remaining.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! The answer was {number}")
            return
        elif guess > number:
            print("Too high.")
            attempts -= 1
        else:
            print("Too low.")
            attempts -= 1
    print("You've run out of guesses, you lose.")

if __name__=="__main__":
    guess_the_number()
