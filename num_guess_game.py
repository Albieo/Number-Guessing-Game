import random
from textwrap import dedent


class GuessingGame():
    welcome_msg = dedent("""
        Welcome to the Number Guessing Game!
        I'm thinking of a number between 1 and 100.
        You have 5 chances to guess the correct number.

        Please select the difficulty level:
        1. Easy (10 chances)
        2. Medium (5 chances)
        3. Hard (3 chances)
    """)

    print(welcome_msg)

    def game():
        try:
            diff_lvl = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")
            return game()

        if diff_lvl not in [1, 2, 3]:
            print("Invalid choice. Please select a difficulty level between 1 and 3.")
            return game()

        number = random.randint(1, 100)
        count = 0

        levels = {1: ("Easy", 10), 2: ("Medium", 5), 3: ("Hard", 3)}
        difficulty, max_attempts = levels[diff_lvl]
        print(f"\nGreat! You have selected the {difficulty} difficulty level. \nLet's start the game!")
        
        while count < max_attempts:
            try:
                guess = int(input("\nEnter your guess: "))
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                continue

            count += 1

            if guess < number:
                print(f"Incorrect! The number is greater than {guess}.")
            elif guess > number:
                print(f"Incorrect! The number is less than {guess}.")            
            else:
                print(f"Congratulations! You guessed the correct number in {count} attempts.")
                break

            if count == max_attempts:
                print(f"Game Over! You failed to guess the number in {max_attempts} guesses. The number was {number}.")
                break
    game()

GuessingGame()
