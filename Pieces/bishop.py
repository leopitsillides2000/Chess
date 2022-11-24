from pieces import Pieces
import numpy as np

class Bishop(Pieces):
    def __init__(self, colour, start_pos, is_alive=True):
        super().__init__(colour, start_pos, is_alive)
        self.name = 'bishop'
        Pieces.board[start_pos[0]][start_pos[1]] = self

    def is_move(self, new_pos):
        pos_dir = new_pos - self.current_pos
        #conditional covers diagonal movement
        if abs(pos_dir[0]) == abs(pos_dir[1]):
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
                    return
                # if own colour exists in new_pos then invalid move
                elif board[new_pos[0]][new_pos[1]].colour == self.colour:
                    print("This is an invalid move. One of your pieces already exists in this position.")
                    return False
                # if opposite colour exists in new_pos then take piece
                else:
                    self.apply_take(new_pos, board)
                    return
            else:
                print("This is an invalid move. A piece is in the way.")
                return False
        else:
            print("This is an invalid move.")
            return False
    