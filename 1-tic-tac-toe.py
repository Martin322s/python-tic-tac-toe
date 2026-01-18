player_one_name = input("Enter the name of Player 1: ")
player_two_name = input("Enter the name of Player 2: ")

player_one_sign = input(f"{player_one_name}, choose your sign (X/O): ").upper()

while player_one_sign not in ['X', 'O']:
    print("Invalid choice. Please choose either X or O.")
    player_one_sign = input(f"{player_one_name}, choose your sign (X/O): ").upper()

player_two_sign = 'O' if player_one_sign == 'X' else 'X'
        
