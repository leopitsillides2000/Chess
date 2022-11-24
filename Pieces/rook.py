from pieces import Pieces
import numpy as np

class Rook(Pieces):
    def __init__(self, colour, start_pos, is_alive=True, has_moved = False):
        super().__init__(colour, start_pos, is_alive)
        self.name = 'rook'
        self.has_moved = has_moved
        Pieces.board[start_pos[0]][start_pos[1]] = self

    def is_move(self, new_pos):
        pos_dir = new_pos - self.current_pos
        #conditional covers vertical/horizontal movement
        if np.all(pos_dir != 0) == False:
            return True
        else:
            return False
    
    def move(self, new_pos, board):
        #check if new_pos is a valid move
        if self.is_move(new_pos) == True:
            #check if any pieces exist between current_pos and new_pos
            if self.simple_check_pos(new_pos, board) == True:
                # if nothing exists in new_pos then move there
                if board[new_pos[0]][new_pos[1]] == None:
                    self.apply_move(new_pos, board)
                    self.has_moved = True #take account for castling
                # if own colour exists in new_pos then invalid move
                elif board[new_pos[0]][new_pos[1]].colour == self.colour:
                    print("This is an invalid move. One of your pieces already exists in this position.")
                # if opposite colour exists in new_pos then take piece
                else:
                    self.apply_take(new_pos, board)
                    self.has_moved = True #take account for castling
            else:
                print("This is an invalid move. A piece is in the way.")
        else:
            print("This is an invalid move.")
    