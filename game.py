"""An implementation of the tic-tac-toe game"""

from random import randint

class Game:
    """A class the implements the tic-tac-toe game
    
    Description:

    attributes:
        player1 (str) : name of player1
        player2 (str) : name of player2
        board (list) : the board
        empty_spots (int) : the count of remaining empty playing spots

    """

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = [[" "] * 3 for _ in range(3)]
        self.empty_spots = 9
    

    def check_mark(self, player):
        """Method to check the mark of the player"""

        # check which player
        if player == self.player1:
            mark = "x"
        else:
            mark = "o"
        
        return mark
    
    def is_valid_coordinate(self, coordinate):
        """Method that returns bool based on valid coordinates"""
        x, y = coordinate

        if x < 0 or x > 2:
            print("Invalid row.")
            return False

        if y < 0 or y > 2:
            print("Invalid column.")
            return False
        
        if self.board[x][y] != " ":
            print("This space has already been taken. Try another space.")
            return False

        return True

    def check_valid_coordinate(self, coordinate):
        """Method to check that a set of coordinates are within range"""

        while not self.is_valid_coordinate(coordinate):
            new_x = input("Please input a valid row. ")
            x = int(new_x)
            new_y = input("Please input a valid column. ")
            y = int(new_y)
            coordinate = (x, y)
        
        return coordinate
    

    def place_mark(self, player, coordinate):
        """Method to help player place their mark on the board"""

        # check which player
        mark = self.check_mark(player)

        # check valid coordinates
        valid_coordinates = self.check_valid_coordinate(coordinate)
        
        # unpack coordinates 
        x, y = valid_coordinates

        # place mark at coordinates
        self.board[x][y] = mark
        self.empty_spots -= 1

        
    

    def start_game(self):
        """Method to determin which player starts"""

        coin_flip = randint(0, 1)
        if coin_flip == 0:
            print(f"{self.player1} starts the game!")
            return self.player1, self.player2
        else:
            print(f"{self.player2} starts the game!")
            return self.player2, self.player1
    

    def check_winner(self, player):
        """Method to check if anyone has one the game"""

        # check which player
        mark = self.check_mark(player)

        # check rows
        for i in range(len(self.board)):
            if not mark in self.board[i]:
                continue
            else:
                row = True
                for j in range(len(self.board[0])):
                    if self.board[i][j] != mark:
                        row = False
                        break
                if row:
                    return True
        
        # check cols
        for i in range(len(self.board[0])):
            col = True
            for j in range(len(self.board)):
                if self.board[j][i] != mark:
                    col = False
                    break
            if col:
                return True
        
        # check positive diagonal
        pos_diag = True
        for i in range(len(self.board)):
            if self.board[i][i] != mark:
                pos_diag = False
                break
        if pos_diag:
            return True
        
        # check negative diagonal
        neg_diag = True
        for j in range(len(self.board)-1, -1, -1):
            if self.board[j][j] != mark:
                neg_diag = False
                break
        if neg_diag:
            return True

        # none of the above conditions met
        return False
    
    def pretty_print_board(self):
        """Method to pretty print the game board."""
        print(self.board[0])
        print(self.board[1])
        print(self.board[2])

    
    def play_round(self, curr_player, second_player):
        """Method to play each round of the game."""

        # print the board
        self.pretty_print_board()

        # input for row and column
        row = input(f"{curr_player}, please select a row to play. ")
        col = input(f"{curr_player}, please select a column to play. ")

        # change type to int
        spot = (int(row), int(col))
        # place mark on spot
        self.place_mark(curr_player, spot)
        # check if there is a winner
        start_win = self.check_winner(curr_player)
        end_win = self.check_winner(second_player)

        # end game if either player wins
        if start_win:
            print(f"{curr_player} wins!")
            return start_win
        if end_win:
            print(f"{second_player} wins!")
            return end_win
        
        return False

    def play_game(self):
        """Method to play a round of the game"""

        # coin flip to chose starting player
        starting_player, ending_player = self.start_game()

        # while there are empty spaces to play, continue game
        while self.empty_spots > 0:
            # play round starting with starting player
            winner = self.play_round(starting_player, ending_player)
            # break loop if winner
            if winner:
                return
            # finish game with there are no empty spaces
            if self.empty_spots == 0:
                print("No winner!")
                return
            # play round with ending player
            winner = self.play_round(ending_player, starting_player)
            # break loop if winner
            if winner:
                return
            
        # if no winner
        print("No winner!")


if __name__ == "__main__":
    p1 = "Me"
    p2 = "You"
    game = Game(p1, p2)

    game.play_game()