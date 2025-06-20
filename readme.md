# Command-Line Calculator

A simple, interactive command-line calculator built with Python. This tool supports basic arithmetic operations, exponentiation, and modulo, with user-friendly prompts and calculation history.

## Features

- Addition, Subtraction, Multiplication, Division
- Exponentiation (`**`)
- Modulo (`%`)
- Calculation history view
- Handles division/modulo by zero gracefully
- Clean, easy-to-read code structure

## Usage

1. **Run the program:**
   ```bash
   python calculator.py
   ```

2. **Follow the prompts:**
   - Enter the first number.
   - Choose an operator from the displayed list.
   - Enter the second number.
   - View the result.

3. **After each calculation:**
   - Enter `y` to perform another calculation.
   - Enter `h` to view calculation history.
   - Enter `q` to quit.

## Example

```
Welcome to the Command-Line Calculator!

Available operators:
  +   : Addition
  -   : Subtraction
  /   : Division
  *   : Multiplication
  .   : Multiplication
  %   : Modulo
  **  : Power

Input first number: 5
Input operator: *
Input second number: 3
Result: 5.0 * 3.0 = 15.0

'y' to continue, 'h' for history, 'q' to exit: h

Calculation History:
  5.0 * 3.0 = 15.0
```

## Requirements

- Python 3.x

## How it Works

The calculator prompts the user for two numbers and an operator, performs the calculation, and displays the result. It keeps a history of all calculations in the session.

## License

This project is open source and free to use for learning and portfolio purposes.

# Number Guessing Game

A fun and interactive command-line game where you try to guess a randomly selected number between 1 and 100 in as few attempts as possible.

## Features

- Random number between 1 and 100 each round
- Friendly prompts and emoji feedback
- Input validation for user guesses
- Tracks number of attempts per game
- Option to play multiple rounds

## How to Play

1. **Run the game:**
   ```bash
   python numbers-game.py
   ```

2. **Game instructions will appear:**
   - The system picks a number between 1 and 100.
   - Enter your guess when prompted.
   - The game will tell you if your guess is too high, too low, or correct.

3. **After winning:**
   - See how many guesses you took.
   - Choose to play again or exit.

## Example

```
==================================================
🎲 Welcome to the Number Guessing Game! 🎲
==================================================
The system has picked a number between 1 and 100.
Try to guess the number in as few attempts as possible.

Enter your guess (1-100): 50
🔻 Too low! Try again.

Enter your guess (1-100): 75
🔺 Too high! Try again.

Enter your guess (1-100): 62

✅ Congratulations! You guessed the number 62 correctly.
🎉 Total guesses: 3

Would you like to play again? (y/n): n
Thank you for playing! Goodbye.
```

## Requirements

- Python 3.x

## License

This project is open source and free to use for learning and portfolio purposes.