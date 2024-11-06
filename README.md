# Number Guessing Game

This is a simple **Number Guessing Game** implemented in Python. The game selects a random number between 1 and 100, and the player has a limited number of chances to guess the correct number based on the chosen difficulty level.

## How to Play

1. When you start the game, you will be greeted with a welcome message explaining the rules.
2. You will be asked to select a difficulty level:
   - **Easy**: 10 chances
   - **Medium**: 5 chances
   - **Hard**: 3 chances
3. Based on the difficulty you choose, you will have a set number of attempts to guess the randomly generated number.
4. Enter your guess, and the game will guide you by indicating whether the correct number is higher or lower than your guess.
5. You win if you guess the number within the allowed attempts. Otherwise, the game ends, revealing the correct number.

## Code Overview

The code contains the following elements:

- **Class**: `GuessingGame` - Represents the game and its structure.
- **Welcome Message**: Explains the game rules and asks for the difficulty level.
- **Difficulty Selection**: Allows the player to choose their difficulty level, impacting the number of attempts.
- **Game Logic**: Checks the player's guesses against the random number and provides hints until the player either guesses correctly or exhausts their attempts.
  
### Error Handling

- Handles invalid inputs when selecting difficulty or entering guesses, ensuring the player provides integers.
  
## Running the Game

1. Ensure you have Python installed (version 3.6+ recommended).
2. Save the code to a file, such as `num_guess_game.py`.
3. Run the game from the command line with:
   ```bash
   python num_guess_game.py
