class Pieces:
    def __init__(self, colour, start_pos, current_pos, is_alive = True):
        self.colour = colour
        self.start_pos = start_pos
        self.current_pos = current_pos
        self.is_alive = is_alive