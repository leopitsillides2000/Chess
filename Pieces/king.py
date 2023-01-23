from pieces import Pieces
import numpy as np

class King(Pieces):
    def __init__(self, colour, start_pos, is_alive=True, has_moved = False, is_check = False):
        super().__init__(colour, start_pos, is_alive)
        self.name = 'king'
        self.has_moved = has_moved
        self.is_check = is_check
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
    ## Ive written it thinking that you move the king to the rook spot and it does the switch
    ## Really you move the king two spaces either side and the castling happens
    ## change this eventually - shouldnt be that hard
    def is_castle(self, new_pos, board):
        diff = self.current_pos - new_pos


        #if king already moved
        if self.has_moved == True:
            return False
        #if new_pos is not two places either side
        elif abs(diff[1]) != 2:
            return False
    
        rook_pos = np.array([self.current_pos[0], 0 if diff[1] > 0 else 7])

        # if piece in rook position is None or not a rook
        if board[rook_pos[0]][rook_pos[1]] == None or board[rook_pos[0]][rook_pos[1]].name != 'rook':
            return False
        #if the rook has moved
        elif board[rook_pos[0]][rook_pos[1]].has_moved == True:
            return False
        #if there is a piece between king and rook
        elif self.simple_check_pos(rook_pos, board) == False:
            return False
        
        return True

    def apply_castle(self, new_pos, board):
        diff = new_pos - self.current_pos

        #changes king
        board[self.current_pos[0]][self.current_pos[1]] = None # sets original king position to None
        self.current_pos = new_pos #changes kings current_pos
        board[self.current_pos[0]][self.current_pos[1]] = self #sets the correct king position


        rook_pos = np.array([self.current_pos[0], 0 if diff[1] < 0 else 7])
        rook = board[rook_pos[0]][rook_pos[1]]
        rook_add = (diff[1]/abs(diff[1])).astype(int)

        #changes rook
        board[new_pos[0]][new_pos[1] - rook_add] = rook # sets new rook position
        board[rook_pos[0]][rook_pos[1]] = None #sets original rook position as empty
        rook.current_pos = np.array([new_pos[0], new_pos[1] - rook_add]) #changes rooks current_pos
        
    def move(self, new_pos, board, apply = True):
        piece = board[new_pos[0]][new_pos[1]]
        if self.is_move(new_pos) == True:
            if piece == None:
                if apply == True:
                    self.apply_move(new_pos, board)
                    self.has_moved == True #taking note for castling
                return True
            elif piece.colour == self.colour:
                print('K')
                print("This is an invalid move. One of your pieces already exists in this position.")
                return False
            else:
                if apply == True:
                    self.apply_take(new_pos, board)
                    self.has_moved == True #taking note for castling
                return True
        elif self.is_castle(new_pos, board) == True and self.is_check == False:
            if apply == True:
                #applying castle
                self.apply_castle(new_pos, board)
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


