from pieces import Pieces
import numpy as np

class King(Pieces):
    def __init__(self, colour, start_pos, current_pos, is_alive=True):
        super().__init__(colour, start_pos, current_pos, is_alive)
        self.name = 'king'
        Pieces.board[start_pos[0]][start_pos[1]] = self

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
        if self.is_move(new_pos) == True:
            if board[new_pos[0]][new_pos[1]] == None:
                self.apply_move(new_pos, board)
            elif board[new_pos[0]][new_pos[1]].colour == self.colour:
                print("This is an invalid move. One of your pieces already exists in this position.")
            else:
                self.apply_take(new_pos, board)
                
        else:
            print("This is an invalid move.")


## Tests

#Regular move
def test1():
    king_white = King('white', np.array([7,4]), np.array([7,4]))
    print(Pieces.board)
    king_white.move(np.array([6,3]), Pieces.board)
    print(Pieces.board)

#Take move
def test2():
    king_white = King('white', np.array([7,4]), np.array([7,4]))
    king_black = King('black', np.array([6,3]), np.array([6,3]))
    print(Pieces.board)
    king_white.move(np.array([6,3]), Pieces.board)
    print(Pieces.board)

#test1()
test2()


