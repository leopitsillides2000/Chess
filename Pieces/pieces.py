import numpy as np

class Pieces:
    board = np.full((8,8), None)
    en_pass = None #keep track of whether en_passant is possible
    en_pass_count = 0
    instances = []

    def __init__(self, colour, start_pos, is_alive = True):
        self.instances.append(self)
        self.colour = colour
        self.start_pos = start_pos
        self.current_pos = start_pos
        self.is_alive = is_alive

    #this simply checks all positions linearly between current_pos and new_pos
    #want to see if any pieces exist in betweeen
    #if they do exist return False as the new_pos is invalid
    def simple_check_pos(self, new_pos, board):
        pos_dir = new_pos - self.current_pos
        #trying to find max of the positive values in pos_dir
        ##dont think this will work as is but same idea
        distance = max(abs(pos_dir))

        #makes pos_dir unit length in terms of chess movement metric
        pos_dir = (pos_dir/distance).astype(int) ##was converting into float

        check_pos = self.current_pos + pos_dir
        #while the space is empty and we havent reached the new posiition keep checking
        while board[check_pos[0]][check_pos[1]] == None and np.array_equal(check_pos, new_pos) == False:
            #add unit direction to check_pos
            check_pos = check_pos + pos_dir
        #outputs True if they are the same and False otherwise
        return np.array_equal(check_pos, new_pos)

    def apply_take(self, new_pos, board):
        #sets previous position to None
        board[self.current_pos[0]][self.current_pos[1]] = None
        #sets oppositions piece to dead
        board[new_pos[0]][new_pos[1]].is_alive = False
        #changes current position
        self.current_pos = new_pos
        #adds piece to new position
        board[new_pos[0]][new_pos[1]] = self

    def apply_move(self, new_pos, board):
        #sets previous position to None
        board[self.current_pos[0]][self.current_pos[1]] = None
        #changes current position
        self.current_pos = new_pos
        #adds piece to new position
        board[new_pos[0]][new_pos[1]] = self