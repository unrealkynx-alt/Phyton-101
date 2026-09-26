# Human, Elephant, Ant

A terminal-based Python implementation of the traditional Indonesian hand game variation of Rock-Paper-Scissors (Gajah, Orang, Semut).

## Rules

- **Elephant** beats **Human**
- **Human** beats **Ant**
- **Ant** beats **Elephant**

If both players choose the same option, it's a tie.

## How to Run

1. Make sure Python 3 is installed.
2. Open your terminal in the project directory.
3. Run the script:
   ```bash
   python rps.py
   ```

## Features

- Case-insensitive input handling (`.lower()`)
- Input validation with error dialogs for invalid inputs
- Session score tracking (wins, losses, ties)
- Clean exit anytime by typing `quit`

## Concepts Practiced

- Functions and return values
- Dictionaries and lists
- While loops, conditionals, break and continue
- Random choice selection via Python's `random` module
