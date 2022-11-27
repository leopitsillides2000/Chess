from pieces import Pieces
import numpy as np

class Queen(Pieces):
    def __init__(self, colour, start_pos, is_alive=True):
        super().__init__(colour, start_pos, is_alive)
        self.name = 'queen'
        Pieces.board[start_pos[0]][start_pos[1]] = self

    def is_move(self, new_pos):
        pos_dir = new_pos - self.current_pos
        #first conditional covers diagonal movement
        #second covers vertical/horizontal movement
        if abs(pos_dir[0]) == abs(pos_dir[1]) or np.all(pos_dir != 0) == False:
            return True
        else:
            return False
    
    def move(self, new_pos, board, apply = True):
        #check if new_pos is a valid move
        if self.is_move(new_pos) == True:
            #check if any pieces exist between current_pos and new_pos
            if self.simple_check_pos(new_pos, board) == True:
                # if nothing exists in new_pos then move there
                if board[new_pos[0]][new_pos[1]] == None:
                    if apply == True:
                        self.apply_move(new_pos, board)
                    return True
                # if own colour exists in new_pos then invalid move
                elif board[new_pos[0]][new_pos[1]].colour == self.colour:
                    print("This is an invalid move. One of your pieces already exists in this position.")
                    return False
                # if opposite colour exists in new_pos then take piece
                else:
                    if apply == True:
                        self.apply_take(new_pos, board)
                    return True
            else:
                print("This is an invalid move. A piece is in the way.")
                return False
        else:
            print("This is an invalid move.")
            return False
    

##Tests

#Regular diagonal move
def test1():
    queen_white = Queen('white', np.array([7,4]))
    print(Pieces.board)
    queen_white.move(np.array([5,2]), Pieces.board)
    print(Pieces.board)

#Regular horizontal move
def test2():
    queen_white = Queen('white', np.array([7,4]))
    print(Pieces.board)
    queen_white.move(np.array([7,2]), Pieces.board)
    print(Pieces.board)

#Piece in the way
def test3():
    queen_white = Queen('white', np.array([7,4]))
    queen_black = Queen('black', np.array([6,3]))
    print(Pieces.board)
    queen_white.move(np.array([5,2]), Pieces.board)
    print(Pieces.board)

#Taking a piece
def test4():
    queen_white = Queen('white', np.array([7,4]))
    queen_black = Queen('black', np.array([5,2]))
    print(Pieces.board)
    queen_white.move(np.array([5,2]), Pieces.board)
    print(Pieces.board)

#test1()



        



