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

    ## Dont know if this is neccessary, will see after next method is written
    def is_valid_move(self, new_pos):
        if (Pawn.is_take_move(new_pos), Pawn.is_reg_move(new_pos), Pawn.is_start_move(new_pos)) == (False, False, False):
            return False
        else:
            return True


    '''
    Just trying to get an idea of how 'board' will be structured.
    Think the best idea would for it to be an 8x8 matrix.
    Each position will contain the piece or None.
    '''

    def move(self, new_pos, board):

        if Pawn.is_reg_move(new_pos) == True:
            # if position is not empty give a invalid message
            if board[new_pos[0]][new_pos[1]].colour != None:
                print("This is an invalid move. A piece already exists in this position.")
            else:
                #sets previous position to None
                board[self.current_pos[0]][self.current_pos[1]] == None
                #changes current position
                self.current_pos == new_pos
        elif Pawn.is_take_move(new_pos) == True:
            # if position is empty either we cant move or it is an en passant
            if board[new_pos[0]][new_pos[1]].colour == None:
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
        elif Pawn.is_start_move(new_pos) == True:
            '''
            ##need to add a bit which check whether all positions in between current_pos and new_pos are empty
            ##will probably need this in every piece except for knights so good to put into method under Pieces class
            pos_dir =  new_pos - self.current_pos
            check_pos = self.current_pos
            for i in range(1, 1+distance):
                check_pos += i*pos_dir
                if board[check_pos[0]][check_pos[1]].colour != None:
                    print("This is an invalid move")
                    break
            '''
            if board[new_pos[0]][new_pos[1]].colour != None:
                print("This is an invalid move. A piece already exists in this position.")
            else:
                #sets previous position to None
                board[self.current_pos[0]][self.current_pos[1]] == None
                #changes current position
                self.current_pos == new_pos
        else:
            print("This is an invalid move. Please try again.")