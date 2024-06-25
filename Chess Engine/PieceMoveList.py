from itertools import product

class PieceMoveList(object):
    def __init__(self, x_board_dim, y_board_dim, number_of_file_spaces, number_of_rank_spaces):
        # used to hold the number of the x dimension of the board
        self.x_board_dim = abs(x_board_dim)
        # used to hold the number of the y dimension of the board
        self.y_board_dim = abs(y_board_dim)
        # how many number of file spaces used in the L-shape calculation
        self.number_of_file_spaces = abs(number_of_file_spaces)
        # how many number of rank spaces used in the L-shape calculation
        self.number_of_rank_spaces = abs(number_of_rank_spaces)

    def l_move_list(self, current_position):
        # get the current position of the knight
        file = current_position[0]
        rank = current_position[1]

        vectors = list(product([0 - self.number_of_file_spaces, 0 + self.number_of_file_spaces],
                               [0 - self.number_of_rank_spaces, 0 + self.number_of_rank_spaces])) + \
                  list(product([0 - self.number_of_rank_spaces, 0 + self.number_of_rank_spaces],
                               [0 - self.number_of_file_spaces, 0 + self.number_of_file_spaces]))
        # position + vectors
        all_moves = [(file + x, rank + y) for x, y in vectors]

        # filter moves outside boundary
        filtered_moves = [(file, rank) for file, rank in all_moves
                          if 1 <= file < self.x_board_dim and 1 <= rank < self.y_board_dim]

        # convert rank and file to new position
        filtered_moves = [[file, rank] for file, rank in filtered_moves]

        return filtered_moves

    def horizontal_move_list(self, current_position):
        # get the current position of the piece
        file = current_position[0]
        rank = current_position[1]

        # only delta in file
        filtered_moves = [[x, rank] for x in range(1, self.x_board_dim+1) if x != file]

        return filtered_moves

    def vertical_move_list(self, current_position):
        # get the current position of the piece
        file = current_position[0]
        rank = current_position[1]

        # only delta in file
        filtered_moves = [[file, y] for y in range(1, self.y_board_dim + 1) if y != rank]

        return filtered_moves