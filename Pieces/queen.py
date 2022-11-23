from pieces import Pieces
import numpy as np

class Queen(Pieces):
    def __init__(self, colour, start_pos, is_alive=True):
        super().__init__(colour, start_pos, is_alive)
        self.name = 'queen'
        Pieces.board[start_pos[0]][start_pos[1]] = self

        def is_move(self, new_pos):
            pos_dir = new_pos - self.current_pos ##current_pos not working? Cos it is not initialised?
            if abs(pos_dir[0]) == abs(pos_dir[1]) or np.all(pos_dir != 0) == False:
                return True
            else:
                return False

        def move(self, new_pos, board):
            if self.is_move(new_pos) == True:
                if self.simple_check_pos(new_pos, board) == True:
                    if board[new_pos[0]][new_pos[1]] == None:
                        self.apply_move(new_pos, board)
                    elif board[new_pos[0]][new_pos[1]].colour == self.colour:
                        print("This is an invalid move. One of your pieces already exists in this position.")
                    else:
                        self.apply_take(new_pos, board)
                else:
                    print("This is an invalid move. A piece is in the way.")
            else:
                print("This is an invalid move.")
                



        



