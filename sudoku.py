# Name:
#      Joshua Sooaemalelagi
#
#      This program is ment to play the game called sudoku. The player can play, load, or save
#      there game and show all values that can be placed in a given square.

# YouTube link for Sudoku demo: https://youtu.be/51DKGPdPues


import json
import sys

_game_over = False
board = []


def main():
    global board
    board = load_game()
    while _game_over == False:
        run_game()


def update_board(col, row, num):
    """
    Updates the game board with given number.

    Parameters:
    - col: Column index (0-8)
    - row: Row index (0-8)
    - num: Number to be placed (1-9)

    Returns:
    None
    """
    global board
    board[row][col] = -num


def load_game():
    """
    Loads the game board data from a JSON file and returns the board as a list.

    Returns:
    The game board as a list.
    """
    difficulty, board_tag = choose_board()
    board = []
    with open('boards.json', 'r') as game_file:
        game_data = json.load(game_file)
        for data in game_data["board"][difficulty][board_tag]:
            board.append(data)
    return board


def save_game():
    """
    Saves the current game board to a JSON file.

    Returns:
    None
    """
    global board
    with open('boards.json', 'r') as game_file:
        game_data = json.load(game_file)
        game_data["board"][3]["Save"] = board
    with open("boards.json", "w") as game_file:
        json.dump(game_data, game_file, indent=2)
    print("\033c", end="")
    print("Game saved!")


def choose_board():
    """
    Allows the user to select a board difficulty.

    Returns:
    - difficulty: Difficulty level (0-2)
    - board_tag: Tag for the selected board
    """
    print("Select board difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Load previous save")

    while True:
        try:
            board_type = int(input(""))
            if board_type in [1, 2, 3, 4]:
                if board_type == 1:
                    board_tag = "Easy"
                elif board_type == 2:
                    board_tag = "Medium"
                elif board_type == 3:
                    board_tag = "Hard"
                elif board_type == 4:
                    board_tag = "Save"
                return board_type - 1, board_tag
            else:
                print("Invalid input. Please enter a number between 1 and 4")
        except ValueError:
            print("Invalid input. Please enter a number")


def get_cheats(col, row, pos):
    """
    Shows all valid inputs for a given square.

    Parameters:
    - col: Column index (0-8)
    - row: Row index (0-8)
    - pos: The string coordinates.

    Returns:
    A list of valid numbers.
    """
    valid_nums = []
    for num_try in range(1, 10):
        if is_play_vaild(col, row, num_try, False) == True:
            valid_nums.append(num_try)
    print("\033c", end="")
    print(valid_nums, end=", ")
    print(f"Showing valid inputs for {pos}")
    return valid_nums


def solve_board():
    """
    Solves the Sudoku board.

    Returns:
    None
    """
    # Add a board solver
    pass


def run_game():
    """
    Plays the Sudoku game.

    Returns:
    None
    """
    global board
    user_input = "--"
    col = 0
    row = 0
    num = 0
    valid_col = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    valid_row = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    try:
        while True:
            display_board()
            user_input = (input(
                "\n 'S' to save game, 'Q' to quit or 'Solve' to finish the board.\n Enter a position to play\n ")).upper()
            if user_input in ["Q", "QUIT"]:
                sys.exit()
            if user_input in ["S", "SAVE"]:
                save_game()
                user_input = "--"
                run_game()
            if user_input == "SOLVE":
                solve_board()
            if len(user_input) != 2:
                print("\033c", end="")
                print("Not a valid input")
                continue
            if user_input[1] in ["A", "B", "C", "D", "E", "F", "G"] and user_input[0] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                user_input = user_input[1]+user_input[0]
            if user_input[0] in ["A", "B", "C", "D", "E", "F", "G"] and user_input[1] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                col = valid_col.index(user_input[0])
                row = valid_row.index(user_input[1])
            else:
                print("\033c", end="")
                print("Invalid input")
                continue

            if check_pos(col, row, board):
                num = input(
                    f" Enter a number to play at position {user_input}?\n or 'C' to show valid inputs at {user_input}.\n").upper()
                if num in ["C", "CHEAT"]:
                    get_cheats(col, row, user_input)
                    run_game()
                if int(num) in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    num = int(num)
                else:
                    print("\033c", end="")
                    print("Invalid number input. Please enter a number between 1 and 9")
                    run_game()
            else:
                continue
            if is_play_vaild(col, row, num):
                update_board(col, row, num)

    except ValueError:
        print("Run_Game Error")


def check_pos(col, row, board, testing=False):
    """
    Checks if the square is empty.

    Parameters:
    - col: Column index (0-8)
    - row: Row index (0-8)
    - board: Game board within a list.
    - testing: Set as true when testing, otherwise default is False.

    Returns:
    True if the square is empty, otherwise False.
    """
    try:
        if board[row][col] == 0:
            return True
        if board[row][col] <= 0:
            erase = input("Do you want to erase this play 'Y' or 'N'").upper()
            if erase in ['Y', 'YES']:
                update_board(row, col, 0)
            return False
        else:
            if testing != True:
                print("\033c", end="")
            print("Cannot play on a played position.")
            return False
    except:
        if testing != True:
            print("\033c", end="")
        print("For positional input, please enter a Column 'A' through 'I' followed by a Row '1' through '9'")
        return False


def is_play_vaild(col, row, num, display_text=True):
    """
    Checks if the play on the given square is valid.

    Parameters:
    - col: Column index (0-8)
    - row: Row index (0-8)
    - num: Number to be placed (1-9)
    - display_text: Optional to display the error messages or not, True by default.

    Returns:
    True if the play is valid, otherwise returns False.
    """
    global board

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i_row in range(start_row, start_row + 3):
        for j_col in range(start_col, start_col + 3):
            if num == board[i_row][j_col] or -num == board[i_row][j_col]:
                if display_text == True:
                    print("\033c", end="")
                    print(f"{num} has already been played in the 3x3 box.")
                return False

    for i in range(9):
        if num == board[i][col] or -num == board[i][col]:
            if display_text == True:
                print("\033c", end="")
                print(f"{num} has already been played in the column.")
            return False
        if num == board[row][i] or -num == board[row][i]:
            if display_text == True:
                print("\033c", end="")
                print(f"{num} has already been played in the row.")
            return False

    return True


def display_board():
    """
    Prints out the Sudoku board.

    Returns:
    None
    """
    global board
    row_count = -1
    print("     A B C   D E F   G H I")
    for row in range(len(board)):
        row_count += 1
        if row_count == 3:
            row_count = 0
            print("   |=======|=======|=======|")
        print(f" {row+1} |", end=" ")
        boarder = 0
        for col in range(len(board[row])):
            boarder += 1
            num = board[row][col]
            if num > 0:
                print(f"\033[31m" + str(num) + "\033[0m", end=" ")
            elif num < 0:
                print(f"\033[34m" + str(abs(num)) + "\033[0m", end=" ")
            else:
                print("_", end=" ")
            if boarder == 3:
                boarder = 0
                print("|", end=" ")
        print()


if __name__ == "__main__":
    main()
