from pieces import Pieces
import numpy as np

class Pawn(Pieces):
    def __init__(self, colour, start_pos, is_alive=True):
        super().__init__(colour, start_pos, is_alive)
        self.name = 'pawn'
        #This puts the piece into its start position on the board
        Pieces.board[start_pos[0]][start_pos[1]] = self

    ## This determines whether the move is a take move for a pawn
    def is_take_move(self, new_pos):
        if self.colour == 'black':
            if np.array_equal(new_pos, self.current_pos + np.array([1,1])) == True or np.array_equal(new_pos, self.current_pos + np.array([1,-1])) == True:
                return True
            else:
                return False
        else:
            if np.array_equal(new_pos, self.current_pos + np.array([-1,-1])) == True or np.array_equal(new_pos, self.current_pos + np.array([-1,1])) == True:
                return True
            else:
                return False


    ## This determines whether the move is just a step forward for the pawn
    def is_reg_move(self, new_pos):
        if self.colour == 'black':
            return np.array_equal(new_pos, self.current_pos + np.array([1,0]))
        else:
            return np.array_equal(new_pos, self.current_pos + np.array([-1,0]))

    ## This determines whether the move is a two step from the start position
    def is_start_move(self, new_pos):
        if np.array_equal(self.start_pos, self.current_pos) == True:
            if self.colour == 'black':
                return np.array_equal(new_pos, self.current_pos + np.array([2,0]))
            else:
                return np.array_equal(new_pos, self.current_pos + np.array([-2,0]))
        else:
            return False

    ## Need to add en passant
    ## is essentially a 'take_move' with extra conditions so could be added later!
    def is_en_passant():
        pass

    def move(self, new_pos, board):

        if self.is_reg_move(new_pos) == True:
            # if position is not empty give an invalid message
            if board[new_pos[0]][new_pos[1]] != None:
                print("This is an invalid move. A piece already exists in this position.")
            else:
                self.apply_move(new_pos, board)
                return
        elif self.is_take_move(new_pos) == True:
            
            # if position is empty either we cant move or it is an en passant
            if board[new_pos[0]][new_pos[1]] == None:
                ## en passant condition
                pass
            # if our piece is in new_pos then this is an invalid move
            elif board[new_pos[0]][new_pos[1]].colour == self.colour:
                print("This is an invalid move. One of your pieces already exists in this position.")
            else:
                self.apply_take(new_pos, board)
                return
        elif self.is_start_move(new_pos) == True:
            #simple_check_pos checks if a piece exists between current_pos and new_pos
            if self.simple_check_pos(new_pos, board) == False:
                print("This is an invalid move. You cannot move over pieces.")
            #if a piece exists in new_pos this move is invalid
            elif board[new_pos[0]][new_pos[1]] != None:
                print("This is an invalid move. A piece already exists in this position.")
            else:
                print(1)
                self.apply_move(new_pos, board)
                return
        else:
            print("This is an invalid move. Please try again.")

##Tests

#regular move forward
def test1():
    pawn_black = Pawn('black', np.array([1,0]))
    print(Pieces.board)
    pawn_black.move(np.array([2,0]), Pieces.board)
    print(Pieces.board)

#double start move
def test2():
    pawn_black = Pawn('black', np.array([1,0]))
    print(Pieces.board)
    pawn_black.move(np.array([3,0]), Pieces.board)
    print(Pieces.board)

#take a piece
def test3():
    pawn_black = Pawn('black', np.array([1,0]))
    pawn_white = Pawn('white', np.array([2,1]))
    print(Pieces.board)
    pawn_black.move(np.array([2,1]), Pieces.board)
    print(Pieces.board)

#test1()
#test2()
test3()