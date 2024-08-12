#making chess
def print_board(board):
    for i in board:
        print("\t\t\t\t"+" | ".join(i))
        print("\t\t\t\t"+"-"*30)

board1 = [["r","h","n","q","k","n","h","r"]
        ,["p","p","p","p","p","p","p","p"]
         ,[" "," "," "," "," "," "," "," "]
         ,[" "," "," "," "," "," "," "," "]
         ,[" "," "," "," "," "," "," "," "]
         ,[" "," "," "," "," "," "," "," "]
         ,["p","p","p","p","p","p","p","p"]
        ,["r","h","n","k","q","n","h","r"]]



print_board(board = board1)