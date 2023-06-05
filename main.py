import random

class ConnectFour:
    def __init__(self):
        self.board = [[' ']*7 for _ in range(6)]
        self.current_player = 'X'

    def print_board(self):
        print('\n'.join([' '.join(row) for row in self.board[::-1]]))
        print(' '.join(map(str, range(1, 8))))

    def is_valid_move(self, col):
        return self.board[5][col] == ' '

    def get_next_open_row(self, col):
        for i in range(6):
            if self.board[i][col] == ' ':
                return i

    def make_move(self, col):
        if not self.is_valid_move(col):
            raise Exception('Invalid move')
        row = self.get_next_open_row(col)
        self.board[row][col] = self.current_player
        if self.check_win():
            print('Player {} wins!'.format(self.current_player))
            self.print_board()
            exit()
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_win(self):
        for row in range(6):
            for col in range(7):
                if self.board[row][col] != ' ' and self.check_starting_point(row, col):
                    return True
        return False

    def check_starting_point(self, row, col):
        return (self.horizontal_check(row, col) or
                self.vertical_check(row, col) or
                self.diagonal_check(row, col))

    def horizontal_check(self, row, col):
        return (col <= 3 and
                self.board[row][col] == self.board[row][col+1] == self.board[row][col+2] == self.board[row][col+3])

    def vertical_check(self, row, col):
        return (row <= 2 and
                self.board[row][col] == self.board[row+1][col] == self.board[row+2][col] == self.board[row+3][col])

    def diagonal_check(self, row, col):
        if row <= 2 and col <= 3 and self.board[row][col] == self.board[row+1][col+1] == self.board[row+2][col+2] == self.board[row+3][col+3]:
            return True
        if row >= 3 and col <= 3 and self.board[row][col] == self.board[row-1][col+1] == self.board[row-2][col+2] == self.board[row-3][col+3]:
            return True
        return False

def play_game():
    game = ConnectFour()
    while True:
        game.print_board()
        if game.current_player == 'X': 
            col = int(input('Player {} enter a column number (1-7): '.format(game.current_player))) - 1
        else:
            col = random.choice([c for c in range(7) if game.is_valid_move(c)])  # Computer makes a random valid move
        if 0 <= col <= 6 and game.is_valid_move(col):
            game.make_move(col)
        else:
            print('Invalid move, try again.')

if __name__ == '__main__':
    play_game()
