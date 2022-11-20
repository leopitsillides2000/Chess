import numpy as np

class Pieces:
    def __init__(self, colour, start_pos, current_pos, is_alive = True):
        self.colour = colour
        self.start_pos = start_pos
        self.current_pos = current_pos
        self.is_alive = is_alive

    #this simply checks all positions linearly between current_pos and new_pos
    #want to see if any pieces exist in betweeen
    #if they do exist return False as the new_pos is invalid
    def simple_check_pos(self, new_pos, board):
        pos_dir = new_pos - self.current_pos
        #trying to find max of the positive values in pos_dir
        ##dont think this will work right now
        distance = max(abs(pos_dir))

        pos_dir = pos_dir/distance

        check_pos = self.current_pos
        while board[check_pos[0]][check_pos[1]] == None or check_pos != new_pos:
            check_pos += pos_dir
        if check_pos != new_pos:
            return False
        else:
            return True