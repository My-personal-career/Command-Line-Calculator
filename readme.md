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