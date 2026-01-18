# Tic Tac Toe (Console) – Python

A classic Tic Tac Toe (3x3) console game for two players, written in Python. The project demonstrates clean game logic, input validation, and the use of custom exceptions.

The game allows two players to enter their names, choose signs (X or O), and take turns placing their symbols on a 3x3 board using positions from 1 to 9. The board numeration is displayed at the start to help players select positions easily.

Players win by placing three of their signs in a row, column, or diagonal. If all positions are filled and no winning condition is met, the game ends in a draw.

Board Numeration:
1 | 2 | 3  
4 | 5 | 6  
7 | 8 | 9  

How to Run:
Make sure you have Python 3 installed. Clone the repository from GitHub, navigate to the project directory, and run the file using the command: python tic_tac_toe.py

The game includes full validation of user input. If a player enters a non-numeric value, a number outside the range 1–9, or selects an already occupied position, a clear and meaningful error message is displayed, and the player is prompted to try again.

Custom Exceptions Used:
InvalidNumberValueError – raised when the input is not a number  
InvalidNumberRangeError – raised when the number is outside the valid range  
PositionAlreadyTakenError – raised when the selected position is already occupied  

These custom exceptions ensure clean control flow and readable, maintainable code.

Technologies:
Python 3, console input/output, exception handling, basic data structures such as lists and dictionaries.

Purpose:
This project is suitable for practicing Python fundamentals, understanding exception handling, implementing game loops, and demonstrating clean and readable code structure.

License:
This project is open-source and free to use for educational purposes.
