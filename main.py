import pyfiglet

columns_dict = {
    "A": 0,
    "B": 1,
    "C": 2,
}

win_conditions = [
    [(0,0), (0,1), (0,2)],
    [(1,0), (1,1), (1,2)],
    [(2,0), (2,1), (2,2)],
    [(0,0), (1,0), (2,0)],
    [(0,1), (1,1), (2,1)],
    [(0,2), (1,2), (2,2)],
    [(0,0), (1,1), (2,2)],
    [(0,2), (1,1), (2,0)]
]

game_over = pyfiglet.figlet_format("Game Over!", font="slant")

def print_title():
    title = pyfiglet.figlet_format("Tic Tac Toe")
    print(title)

    print("""
        How to play:
        - Players take turns placing their mark
        - Enter your move as Row-Column e.g. 1-A
        - Rows: 1, 2, 3 | Columns: A, B, C
        - First to get 3 in a row wins!

        Example board:

              A   B   C
            +---+---+---+
          1 | X |   |   |
            +---+---+---+
          2 |   | O |   |
            +---+---+---+
          3 |   |   | X |
            +---+---+---+
    """)

def clean_input(user_input):
    alphanum_list = [char for char in user_input if char.isalnum()]
    cleaned_input = "".join(alphanum_list)
    return cleaned_input

def draw_board(board):
    print(f"""
          A   B   C
        +---+---+---+
      1 | {board[0][0]} | {board[0][1]} | {board[0][2]} |
        +---+---+---+
      2 | {board[1][0]} | {board[1][1]} | {board[1][2]} |
        +---+---+---+
      3 | {board[2][0]} | {board[2][1]} | {board[2][2]} |
        +---+---+---+
    """)

def win_condition(board, player):
    for condition in win_conditions:
        if all(board[r][c] == player[1] for r, c in condition):
            return True
    return False

def play_game():
    player = ("1", "X")
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    print_title()
    while True:

        input_valid = False
        while not input_valid:
            try:
                player_input = input(f"Player {player[0]} ({player[1]}) - Choose a cell: ").upper()
                final_input = clean_input(player_input)

                if board[(int(final_input[0]) - 1)][columns_dict[final_input[1]]] != " ":
                    raise Exception("Invalid placement. The cell you chose is already occupied. Choose another cell")

                board[(int(final_input[0]) - 1)][columns_dict[final_input[1]]] = player[1]

                input_valid = True

            except (KeyError, ValueError, IndexError):
                print("Invalid input. Please ensure your input follows this format: 1-A")
            except Exception as e:
                print(e)

        draw_board(board)

        if win_condition(board, player):
            print(game_over)
            print(f"Congrats! Player {player[0]} won!")
            break

        if all(value != " " for nested_list in board for value in nested_list):
            print(game_over)
            print("It's a draw! Better luck next time...")
            break

        if player == ("1", "X"):
            player = ("2", "O")
        else:
            player = ("1", "X")

play_again = True
while play_again:
    play_game()
    answer = input("Play again? (Y/N): ")
    play_again = answer.upper() == "Y"