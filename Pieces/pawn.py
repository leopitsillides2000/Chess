from pieces import Pieces
import numpy as np


class Pawn(Pieces):
    def __init__(self, colour, start_pos, current_pos, is_alive=True):
        super().__init__(colour, start_pos, current_pos, is_alive)
        self.name = 'pawn'

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

    '''
    Just trying to get an idea of how 'board' will be structured.
    Think the best idea would be an 8x8 numpy matrix.
    Each position will contain the a piece object or None.
    '''

    def move(self, new_pos, board):

        if Pawn.is_reg_move(new_pos) == True:
            # if position is not empty give an invalid message
            if board[new_pos[0]][new_pos[1]] != None:
                print("This is an invalid move. A piece already exists in this position.")
            else:
                #sets previous position to None
                board[self.current_pos[0]][self.current_pos[1]] == None
                #changes current position
                self.current_pos == new_pos
                #adds piece to new position
                board[new_pos[0]][new_pos[1]] == self
        elif Pawn.is_take_move(new_pos) == True:
            # if position is empty either we cant move or it is an en passant
            if board[new_pos[0]][new_pos[1]] == None:
                ## en passant condition
                pass
            # if our piece is in new_pos then this is an invalid move
            elif board[new_pos[0]][new_pos[1]].colour == self.colour:
                print("This is an invalid move. One of your pieces already exists in this position.")
            else:
                #sets previous position to None
                board[self.current_pos[0]][self.current_pos[1]] == None
                #sets oppositions piece to dead
                board[new_pos[0]][new_pos[1]].is_alive == False
                #changes current position
                self.current_pos == new_pos
                #adds piece to new position
                board[new_pos[0]][new_pos[1]] == self
        elif Pawn.is_start_move(new_pos) == True:
            #simple_check_pos checks if a piece exists between current_pos and new_pos
            if Pieces.simple_check_pos(new_pos, board) == False:
                print("This is an invalid move. You cannot move over pieces.")
            #if a piece exists in new_pos this move is invalid
            elif board[new_pos[0]][new_pos[1]] != None:
                print("This is an invalid move. A piece already exists in this position.")
            else:
                #sets previous position to None
                board[self.current_pos[0]][self.current_pos[1]] == None
                #changes current position
                self.current_pos == new_pos
                #adds piece to new position
                board[new_pos[0]][new_pos[1]] == self
        else:
            print("This is an invalid move. Please try again.")