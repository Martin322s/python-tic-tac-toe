class InvalidNumberValueError(Exception):
    pass

class InvalidNumberRangeError(Exception):
    pass

class PositionAlreadyTakenError(Exception):
    pass

position_mapper = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2)
}

def read_players_data():
    player_one_name = input("Enter the name of Player 1: ")
    player_two_name = input("Enter the name of Player 2: ")

    player_one_sign = input(f"{player_one_name}, choose your sign (X/O): ").upper()

    while player_one_sign not in ['X', 'O']:
        print("Invalid choice. Please choose either X or O.")
        player_one_sign = input(f"{player_one_name}, choose your sign (X/O): ").upper()

    player_two_sign = 'O' if player_one_sign == 'X' else 'X'

    print(f"{player_one_name} will be '{player_one_sign}' and {player_two_name} will be '{player_two_sign}'.")
    print(f"{player_one_name} starts first.")

    return ((player_one_name, player_one_sign), (player_two_name, player_two_sign))

def print_board_numeration():
    print("This is the numeration for the Tic Tac Toe board: ")
    print(" 1 | 2 | 3 ")
    print(" 4 | 5 | 6 ")
    print(" 7 | 8 | 9 ")

def print_game_board(board):
    for row in board:
        print(" |" + " | ".join(row) + "|")

def check_winner(board, sign):
    for row in board:
        if all(cell == sign for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return True
    if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
        return True
    return False

def check_position(position, board):
    try:
        position = int(position)
    except ValueError:
        raise InvalidNumberValueError("The position must be a number between 1 and 9.")
    
    if position < 1 or position > 9:
        raise InvalidNumberRangeError("The position must be a number between 1 and 9.")
    
    row_index, col_index = position_mapper[position]

    if board[row_index][col_index] != ' ':
        raise PositionAlreadyTakenError("This position is already taken. Please choose another one.")
    
    return (row_index, col_index)

def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)

board = [[' ', ' ', ' '] for _ in range(3)]
player_one_data, player_two_data = read_players_data()
print_board_numeration()
turns = 1

while True:
    current_player_name, current_player_sign = player_one_data if turns % 2 != 0 else player_two_data
    position = input(f"{current_player_name}, enter free the position (1-9) where you want to place your sign: ")

    try:
        row_index, col_index = check_position(position, board)
    except (InvalidNumberValueError, InvalidNumberRangeError) as e:
        print(e)
        continue
    except PositionAlreadyTakenError as e:
        print(e)
        continue
    else:
        board[row_index][col_index] = current_player_sign
        print_game_board(board)
        turns += 1

    if check_draw(board):
        print("The game is a draw!")
        break

    if check_winner(board, current_player_sign):
        print(f"Congratulations {current_player_name}! You have won the game!")
        break