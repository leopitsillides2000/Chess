from pieces import Pieces
import numpy as np

class King(Pieces):
    def __init__(self, colour, start_pos, is_alive=True, has_moved = False):
        super().__init__(colour, start_pos, is_alive)
        self.name = 'king'
        self.has_moved = has_moved
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


    ## This is not completely right
    ## Ive written it thinking that you move the queen to the rook spot and it does the switch
    ## Really you move the queen two spaces either side and the castling happens
    ## change this eventually - shouldnt be that hard
    def is_castle(self, new_pos, board):
        piece = board[new_pos[0]][new_pos[1]]
        #if new_pos has rook
        if piece != None and piece.name == 'rook':
            #if rook is the same colour
            if self.colour == piece.colour:
                #if neither rook nor king have moved, return True
                if piece.has_moved == False and self.has_moved == False:
                    #if there are no pieces between the king and the rook
                    if self.simple_check_pos(new_pos, board) == True:
                        return True
        return False
        
    def move(self, new_pos, board, apply = True):
        piece = board[new_pos[0]][new_pos[1]]
        if self.is_move(new_pos) == True:
            if piece == None:
                if apply == True:
                    self.apply_move(new_pos, board)
                    self.has_moved == True #taking note for castling
                return True
            elif piece.colour == self.colour:
                print("This is an invalid move. One of your pieces already exists in this position.")
                return False
            else:
                if apply == True:
                    self.apply_take(new_pos, board)
                    self.has_moved == True #takingnote for castling
                return True
        elif self.is_castle(new_pos, board) == True:
            if apply == True:
                ## this is NOT right!! they dont go to each others position
                pos_dir = new_pos - self.current_pos
                pos_dir_hat = (pos_dir / abs(pos_dir[1])).astype(int) # this is to get a unit directional vector since we know only horizontal
                #changes king
                board[self.current_pos[0]][self.current_pos[1]] = None # sets original king position to None
                self.current_pos = self.current_pos + 2*pos_dir_hat #changes kings current_pos
                board[self.current_pos[0]][self.current_pos[1]] = self #sets the correct king position
                #changes rook
                board[new_pos[0]][new_pos[1]] = None # sets original rook position as empty
                piece.current_pos = self.current_pos - pos_dir_hat #changes rooks current_pos
                board[piece.current_pos[0]][piece.current_pos[1]] = piece # sets new rook position

                self.has_moved = True # taking note for castling
            return True
        else:
            print("This is an invalid move.")
            return False


## Tests

#Regular move
def test1():
    king_white = King('white', np.array([7,4]))
    print(Pieces.board)
    king_white.move(np.array([6,3]), Pieces.board)
    print(Pieces.board)

#Take move
def test2():
    king_white = King('white', np.array([7,4]))
    king_black = King('black', np.array([6,3]))
    print(Pieces.board)
    king_white.move(np.array([6,3]), Pieces.board)
    print(Pieces.board)
    print(king_white.current_pos)

def test3():
    king_white = King('white', np.array([7,4]))
    print(Pieces.board)
    king_white.move(np.array([5,4]), Pieces.board)
    print(Pieces.board)

def test_castle():
    from rook import Rook
    from bishop import Bishop

    king_white = King('white', np.array([7,4]))
    rook_white = Rook('white', np.array([7,7]))
    bishop_white = Bishop('white', np.array([7,5]))

    print(Pieces.board)
    king_white.move(np.array([7,7]), Pieces.board)
    print(Pieces.board)

#test1()
#test2()
#test3()
#test_castle()


