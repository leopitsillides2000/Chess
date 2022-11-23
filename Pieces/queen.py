from pieces import Pieces
import numpy as np

class Queen(Pieces):
    def __init__(self, colour, start_pos, is_alive=True):
        super().__init__(colour, start_pos, is_alive)
        self.name = 'queen'
