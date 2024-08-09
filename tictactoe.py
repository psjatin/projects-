import itertools
def print_board(board):
    """will print the board..."""
    for i in board:
        print(' | '.join(i))
        print("-"*9)
# row , col = 3,3

def check_win(board,mark):
    """will take the mark and check rows
    columns and diagnals to be same..."""
    #checking rows
    for i in board:
        if i.count(mark) == 3:
            return True
    #checking columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == mark:
            return True

    #checking uniform diagnol
    # for i in range(3):
    if [board[i][i] for i in range(3)].count(mark) == 3:
        return True
    if [board[i][2-i] for i in range(3)].count(mark) == 3:
        return True
    return False


# lis = [["" for i in range(3)] for i in range(3)]
# print(lis)
# lis[row][column] = "X"
# print(lis)
def change_player(current):
    """Change the player from X to O or O to X."""
    return "O" if current == "X" else "X"

def tie_game(board):
    """will check for game to tie"""
    if all(i != " " for row in board for i in row):
        return True
    return False

board = [[" " for i in range(3)] for i in range(3)]
current_player = "X"
while True:
    print_board(board)
    print(f"Your turn {current_player}, Make a move..")
    try:
        print("Enter Row and Column (separated by a space):")
        r, c = map(int, input().split())
        if board[r - 1][c - 1] != " ":
            print("That position is already taken. Try again.")
            continue
    except ValueError:
        print("INVALID ENTRY ENTERED...")
        continue
    board[r-1][c-1] = current_player
    result = check_win(board,current_player)
    if result:
        print(print_board(board))
        print(f"{current_player} won the match")
        break

    if tie_game(board):
        print(print_board(board))
        print("The match is a draw..")
    current_player = change_player(current_player)















