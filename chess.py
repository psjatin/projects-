#making chess
# def print_board(board):
#     for i in board:
#         print("\t\t\t\t"+" | ".join(i))
#         print("\t\t\t\t"+"-"*30)
board1 = [["r","h","n","q","k","n","h","r"]
        ,["p","p","p","p","p","p","p","p"]
         ,[" "," "," "," "," "," "," "," "]
         ,[" "," "," "," "," "," "," "," "]
         ,[" "," "," "," "," "," "," "," "]
         ,[" "," "," "," "," "," "," "," "]
         ,["p","p","p","p","p","p","p","p"]
        ,["r","h","n","k","q","n","h","r"]]



# print_board(board = board1)
class chess:
     def __init__(self):
         self.board = self.initialise_board(board1)
         self.current_player = "White"

     def initialise_board(self,board):
         for i in board:
             print("\t\t\t\t" + " | ".join(i))
             print("\t\t\t\t" + "-" * 30)

     def display_board(self,board):
         print(self.board)
     def is_game_over(self):
         return False
     def play(self):
         while not self.is_game_over():
             pass
     def valid_move(self , row,col,row2,col2):
         # for pawn
         pawn = rook = bishop = king = queen = horse = False
         if self.empty_shell(row2,col2):
             if board1[row][col] == "p":
                pawn = True





     def empty_shell(self,row,col):
         if board1[row][col] != " ":
             print("Shell already taken...")
             return True
         return False












     def board_marking(self):
         a,b,c,d,e,f,g,h = 1,2,3,4,5,6,7,8






game = chess()

