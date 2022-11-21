from pieces import Pieces
import numpy as np

class King(Pieces):
    def __init__(self, colour, start_pos, current_pos, is_alive=True):
        super().__init__(colour, start_pos, current_pos, is_alive)
        self.name = 'king'

    #all moves for king are take moves
    def is_move(self, new_pos):
    
        pos_dir = new_pos - self.current_pos
        #if valid the vector pos_dir should be some variation of [1|0|-1, 1|0|-1], e.g. [1,-1]
        #when dotted with itself it will not be greater than 2
        #but any other position in the board will give a dot porduct greater than 2
        if np.dot(pos_dir, pos_dir) <= 2:
            return True
        else:
            return False

    def move(self, new_pos, board):
        if King.is_move(new_pos) == True:
            if board[new_pos[0]][new_pos[1]].colour == self.colour: #dont know whats up here?
                print("This is an invalid move. One of your pieces already exists in this position.")
            elif board[new_pos[0]][new_pos[1]] != None:
                #sets previous position to None
                board[self.current_pos[0]][self.current_pos[1]] == None
                #sets oppositions piece to dead
                board[new_pos[0]][new_pos[1]].is_alive == False
                #changes current position
                self.current_pos == new_pos
                #adds piece to new position
                board[new_pos[0]][new_pos[1]] == self
            else:
                #sets previous position to None
                board[self.current_pos[0]][self.current_pos[1]] == None
                #changes current position
                self.current_pos == new_pos
                #adds piece to new position
                board[new_pos[0]][new_pos[1]] == self
        else:
            print("This is an invalid move.")

