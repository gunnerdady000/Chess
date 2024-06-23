# Author: Runner
# Date: 6/22/2024
# Purpose: Create a Chess engine to be used for different bot algorithms
import numpy as np


class Space:
    def __init__(self, color, board_space, occupying_piece):
        # white or black
        self.color = color
        # location of space on board
        self.board_space = board_space
        # piece occupying the space
        self.occupying_piece = occupying_piece

    def update_piece(self, occupying_piece):
        self.occupying_piece = occupying_piece


class MyEngine:
    def __init__(self):
        None

    # create board
    def create_board(self):
        # 8x8 array
        # row 1, White non-pawns
        row_1 = np.array([Space("Black", "a1", "WhiteRook"), Space("White", "b1", "WhiteKnight"),
                          Space("Black", "c1", "WhiteBishop"), Space("White", "d1", "WhiteQueen"),
                          Space("Black", "e1", "WhiteKing"), Space("White", "f1", "WhiteBishop"),
                          Space("Black", "g1", "WhiteKnight"), Space("White", "h1", "WhiteRook")])
        # row 2, White pawns
        # row_2 = np.array([])
        # rows 3 - 6 blank
        # rows_3to6 = np.array([])
        # row 7, Black pawns
        # row_7 = np.array([])
        # row 8, Black non-pawns
        # row_8 = np.array([])
        # shove into board
        # self.board = np.vstack()
    def ascii_board(self):
        # 8x8 board
        None

    # rook piece

    # knight piece

    # bishop piece

    # queen piece

    # king piece


def main():
    Chess = MyEngine()
    Chess.create_board()
    print("Done")


# Using the special variable
# __name__
if __name__ == "__main__":
    main()