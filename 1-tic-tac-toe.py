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

board = [[' ', ' ', ' '] for _ in range(3)]
player_one_data, player_two_data = read_players_data()
print_board_numeration()
turns = 1

while True:
    current_player_name, current_player_sign = player_one_data[0] if turns % 2 != 0 else player_two_data[0]
    try:
        position = input(f"{current_player_name}, enter free the position (1-9) where you want to place your sign: ")
        position = int(position)
    except ValueError:
        print("Invalid input. Please enter a valid number between 1 and 9.")
        continue

    if position < 1 or position > 9:
        print("Invalid position. Please choose a number between 1 and 9.")
        continue

    row, col = position_mapper[position]  