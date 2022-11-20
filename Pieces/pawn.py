from pieces import Pieces
import numpy as np


## going to write it for whites first!!
## everythigng
class Pawn(Pieces):
    def __init__(self, colour, start_pos, current_pos, is_alive=True):
        super().__init__(colour, start_pos, current_pos, is_alive)

    ## This determines whether the move is a take move for a pawn
    def is_take_move(self, new_pos):
        if new_pos == self.current_pos + np.array([1,1]) or new_pos == self.current_pos + np.array([1,-1]):
            return True
        else:
            return False

    ## This determines whether the move is just a step forward for the pawn
    def is_reg_move(self, new_pos):
        if new_pos == self.current_pos + np.array([1,0]):
            return True
        else:
            return False

    ## This determines whether the move is a two step from the start position
    def is_start_move(self, new_pos):
        if new_pos == self.current_pos + np.array([2,0]) and self.start_pos == self.current_pos:
            return True
        else:
            return False

    ## Need to add en passant
    ## is essentially a 'take_move' with extra conditions so could be added later!
    def is_en_passant():
        pass


    def is_valid_move(self, new_pos, board):

        if board[new_pos[0]][new_pos[1]] == None:
            continue
        elif:

        
        if self.start_pos == self.current_pos:
            # can move two spaces

