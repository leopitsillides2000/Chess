from pieces import Pieces
from pawn import Pawn
from king import King
from queen import Queen
from bishop import Bishop
from rook import Rook
from knight import Knight
import numpy as np


class Game():
    def __init__(self):
        pawn_w1 = Pawn('white', np.array([6,0]))
        pawn_w2 = Pawn('white', np.array([6,1]))
        pawn_w3 = Pawn('white', np.array([6,2]))
        pawn_w4 = Pawn('white', np.array([6,3]))
        pawn_w5 = Pawn('white', np.array([6,4]))
        pawn_w6 = Pawn('white', np.array([6,5]))
        pawn_w7 = Pawn('white', np.array([6,6]))
        pawn_w8 = Pawn('white', np.array([6,7]))
        rook_w1 = Rook('white', np.array([7,0]))
        rook_w2 = Rook('white', np.array([7,7]))
        knight_w1 = Knight('white', np.array([7,1]))
        knight_w2 = Knight('white', np.array([7,6]))
        bishop_w1 = Bishop('white', np.array([7,2]))
        bishop_w2 = Bishop('white', np.array([7,5]))
        queen_w = Queen('white', np.array([7,3]))
        king_w = King('white', np.array([7,4]))
        pawn_b1 = Pawn('black', np.array([1,0]))
        pawn_b2 = Pawn('black', np.array([1,1]))
        pawn_b3 = Pawn('black', np.array([1,2]))
        pawn_b4 = Pawn('black', np.array([1,3]))
        pawn_b5 = Pawn('black', np.array([1,4]))
        pawn_b6 = Pawn('black', np.array([1,5]))
        pawn_b7 = Pawn('black', np.array([1,6]))
        pawn_b8 = Pawn('black', np.array([1,7]))
        rook_b1 = Rook('black', np.array([0,0]))
        rook_b2 = Rook('black', np.array([0,7]))
        knight_b1 = Knight('black', np.array([0,1]))
        knight_b2 = Knight('black', np.array([0,6]))
        bishop_b1 = Bishop('black', np.array([0,2]))
        bishop_b2 = Bishop('black', np.array([0,5]))
        queen_b = Queen('black', np.array([0,3]))
        king_b = King('black', np.array([0,4]))
        print(Pieces.board)

    def mate():
        pass
    
    def check_mate():
        pass

    def stale_mate():
        pass

    def run_game(self):
        white_or_black = 0

        while self.check_mate() == False and self.stale_mate() == False:
            #keeps track of en passant
            Pieces.en_pass_count += 1
            #just need to determine whos turn it is
            if white_or_black  == 0:
                colour = 'white'
                #changes players turn
                white_or_black += 1
            else:
                colour = 'black'
                #changes players turn
                white_or_black -= 1
            piece_pos = input("Please input a piece position as a list [row, column]: ")
            while Pieces.board[piece_pos[0]][piece_pos[1]] == None or Pieces.board[piece_pos[0]][piece_pos[1]].colour != colour:
                piece_pos = input("This input was invalid, please try again: ")
            piece = Pieces.board[piece_pos[0]][piece_pos[1]]
            new_pos = input("Please input a position you wish to move to as a list [row, column]: ")
            while piece.move(new_pos, Pieces.board) == False:
                new_pos = input("The move you entered was invalid. Please try again: ")
            
            continue
        pass


game = Game()




