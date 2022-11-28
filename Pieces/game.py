from pieces import Pieces
from pawn import Pawn
from king import King
from queen import Queen
from bishop import Bishop
from rook import Rook
from knight import Knight
import numpy as np


class Game():
    def __init__(self):
        ##might need to add self before all of these
        pawn_w1 = Pawn('white', np.array([6,0]))
        pawn_w2 = Pawn('white', np.array([6,1]))
        pawn_w3 = Pawn('white', np.array([6,2]))
        pawn_w4 = Pawn('white', np.array([6,3]))
        pawn_w5 = Pawn('white', np.array([6,4]))
        pawn_w6 = Pawn('white', np.array([6,5]))
        pawn_w7 = Pawn('white', np.array([6,6]))
        pawn_w8 = Pawn('white', np.array([6,7]))
        rook_w1 = Rook('white', np.array([7,0]))
        rook_w2 = Rook('white', np.array([7,7]))
        knight_w1 = Knight('white', np.array([7,1]))
        knight_w2 = Knight('white', np.array([7,6]))
        bishop_w1 = Bishop('white', np.array([7,2]))
        bishop_w2 = Bishop('white', np.array([7,5]))
        queen_w = Queen('white', np.array([7,3]))
        self.king_w = King('white', np.array([7,4]))
        pawn_b1 = Pawn('black', np.array([1,0]))
        pawn_b2 = Pawn('black', np.array([1,1]))
        pawn_b3 = Pawn('black', np.array([1,2]))
        pawn_b4 = Pawn('black', np.array([1,3]))
        pawn_b5 = Pawn('black', np.array([1,4]))
        pawn_b6 = Pawn('black', np.array([1,5]))
        pawn_b7 = Pawn('black', np.array([1,6]))
        pawn_b8 = Pawn('black', np.array([1,7]))
        rook_b1 = Rook('black', np.array([0,0]))
        rook_b2 = Rook('black', np.array([0,7]))
        knight_b1 = Knight('black', np.array([0,1]))
        knight_b2 = Knight('black', np.array([0,6]))
        bishop_b1 = Bishop('black', np.array([0,2]))
        bishop_b2 = Bishop('black', np.array([0,5]))
        queen_b = Queen('black', np.array([0,3]))
        self.king_b = King('black', np.array([0,4]))
        #print(Pieces.board)
    
    #this just gives a nicer representation of the board for visual aid
    def nice_board(self):
        nice_board = np.full((8,8), None)
        for i in range(8):
            for j in range(8):
                if Pieces.board[i][j] != None:
                    #nice_board[i][j] = np.array([Pieces.board[i][j].name[:2].title(), Pieces.board[i][j].colour[:1].title()])
                    nice_board[i][j] = Pieces.board[i][j].name[:2].title() + '_' + Pieces.board[i][j].colour[:1].title()
                else:
                    nice_board[i][j] = '____'

        print(nice_board)

    #this checks for check in all scenarios
    ## just need to add possible knight threat
    def is_check(self, king, prev_new_pos):

        #check to see if threat by knight
        if Pieces.board[prev_new_pos[0]][prev_new_pos[1]].name == 'knight':
            if Pieces.board[prev_new_pos[0]][prev_new_pos[1]].move(king.current_pos, Pieces.board, apply = False) == True:
                return True

        # Lambda function to change through the different angles
        dir = lambda angle: np.around(np.array([np.sin(angle), np.cos(angle)])/max(abs(np.array([np.cos(angle), np.sin(angle)])))).astype(int)
        #Changes to True if king is under threat
        any_threat = False

        #this is the angle to change the dir lambda function
        theta = 0
        #keep going until 1/8 turn around the unit circle is checked
        while theta < 2*np.pi:
            #sets position that is being checked
            pos = king.current_pos + dir(theta)
            #keep going while the position is still within the board
            while 0 <= pos[0] < 8 and 0 <= pos[1] < 8:
                #if space is non-empty
                if Pieces.board[pos[0]][pos[1]] != None:
                    #if colour is same return False
                    if Pieces.board[pos[0]][pos[1]].colour == king.colour:
                        break
                    else:
                        #if colour is opposite and the take on king is valid any_threat = True
                        if Pieces.board[pos[0]][pos[1]].move(king.current_pos, Pieces.board, apply = False) == True:
                            any_threat = True
                        break
                else:
                    #adjusts the position along the direction
                    pos = pos + dir(theta)
            #adds 1/8 turn to theta to check the next direction
            theta = theta + np.pi/4
        #print(any_threat)
        return any_threat

        
    '''
    ###OLD is_check ###
    def is_check(self, king, piece_pos, new_pos, prev_current_pos, prev_new_pos):
        #print(Pieces.board[prev_new_pos[0]][prev_new_pos[1]].name)
        #if the previously moved piece can attack the current king, return True
        if Pieces.board[prev_new_pos[0]][prev_new_pos[1]].move(king.current_pos, Pieces.board, apply = False) == True:
            return True

        # if moved pieces original position(piece_pos) was blocking an attack to king
        #finding direction between king and moved piece
        pos_dir = piece_pos - king.current_pos
        pos_dir_hat = (pos_dir/(max(abs(pos_dir)))).astype(int)
        #if the direction between king and moved piece is either not diagonal or horizontal/vertical then return False
        if np.dot(pos_dir_hat, pos_dir_hat) != 2 and np.dot(pos_dir_hat, pos_dir_hat) != 1:
            return False
        else:
            pos = king.current_pos + pos_dir_hat
            print(pos)
            #while pos is within the board
            while 0<=pos[0]<=8 and 0<=pos[1]<=8:
                #if space is non-empty
                if Pieces.board[pos[0]][pos[1]] != None:
                    #if colour is same return False
                    if Pieces.board[pos[0]][pos[1]].colour == king.colour:
                        return False
                        break
                    else:
                        #if colour is opposite and the take on king is valid return True
                        if Pieces.board[pos[0]][pos[1]].move(king.current_pos, Pieces.board, apply = False) == True:
                            return True
                        break
                    break
                pos = pos + pos_dir_hat
            return False

        #need to check if king is the one that moved whether it has moved into a position which is check

        #need to also check for knights, this might need to be at the beginning!

        #need to put threat if castling

        

        ##Needs filling in
        
        #check

        return False
        '''
    
    def is_check_mate(self):
        ##Needs filling in
        return False

    def is_stale_mate(self):
        ##Needs filling in
        return False

    def is_valid_input(self, pos):
        try:
            #checks if inputs are integers
            if all(isinstance(element, int) for element in pos):
                #checks if they are within boounds of the board
                if 0 <= pos[0] < 8 and 0 <= pos[1] < 8:
                    return True
                else:
                    ValueError("The position must be within the board, that is 0-7 for each input")
            else:
                raise ValueError('All elements inside your list are not integers')

        except ValueError as error:
            print('Caught an error: ' + repr(error))
            return False

        

    def run_game(self):
        white_or_black = 0
        new_pos = [0,0]

        #previous new_pos for determining knight check
        prev_new_pos = np.array([0,0])

        while self.is_check_mate() == False and self.is_stale_mate() == False:
            #printing visually easy board
            self.nice_board()

            #keeps track of en passant
            Pieces.en_pass_count += 1
            #just need to determine whos turn it is

            #break clause if player wants to start again
            if new_pos != [-1,-1]:
                #making sure its the correct colours turn
                if white_or_black  == 0:
                    colour = 'white'
                    #changes players turn
                    white_or_black += 1
                    #sets kings for whites go, used for check/checkmate etc.
                    king = self.king_w
                else:
                    colour = 'black'
                    #changes players turn
                    white_or_black -= 1
                    #sets kings for blacks go, used for check/checkmate etc.
                    king = self.king_b
                print(f"It is {colour} players turn.")

            #Gets input from player
            ## Would make more sense to put this in an np array for consistency
            piece_pos = [int(input("Please input the row of the piece position: ")), int(input("Please input the column of the piece position: "))]
            #repeat if input is invalid, the input is not a piece, or the piece is not the right colour
            while self.is_valid_input(piece_pos) == False or Pieces.board[piece_pos[0]][piece_pos[1]] == None or Pieces.board[piece_pos[0]][piece_pos[1]].colour != colour:
                print("This input is invalid, please try again.")
                piece_pos = [int(input("Please input the row of the piece position: ")), int(input("Please input the column of the piece position: "))]
            
            #create a piece variable, remeber board cant be adapted from this variable
            piece = Pieces.board[piece_pos[0]][piece_pos[1]]

            #Option to start the choices again by entering [-1,-1]
            print("If you would like to start your choices again please enter -1 then -1 again.")
            #Gets input from player for desired new position
            new_pos = [int(input("Please input the row of the new position: ")), int(input("Please input the column of the new position: "))]
            
            if new_pos != [-1,-1]:
                while self.is_valid_input(new_pos) == False or piece.move(np.array(new_pos), Pieces.board, apply = False) == False:
                    print("This input is invalid, please try again.")
                    new_pos = [int(input("Please input the row of the new position: ")), int(input("Please input the column of the new position: "))]
                    if new_pos == [-1, -1]:
                        break

            if new_pos != [-1,-1]:
                #remember what was in theh new space in case we have to revert
                space = Pieces.board[new_pos[0]][new_pos[1]]
                #move the piece
                piece.move(np.array(new_pos), Pieces.board)
                #if king is in check
                if self.is_check(king, prev_new_pos) == True:
                    #reset the board to previous one
                    Pieces.board[piece_pos[0]][piece_pos[1]] = piece
                    Pieces.board[new_pos[0]][new_pos[1]] = space

                    #start the go again
                    new_pos = [-1, -1]
                    print("This move is invalid. There is a check on the King.")
                else:

                    #set prev_current_pos and prev_new_pos to memory for knight check
                    prev_new_pos = np.array(new_pos)
            
        print('The game has ended!')


game = Game()
game.run_game()



