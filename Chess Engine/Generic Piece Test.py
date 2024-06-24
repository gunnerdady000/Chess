from GenericPiece import GenericPiece


def knight_test(piece, cur_pos):
    piece.move_lshape(cur_pos, "NNW", 1, 2)
    piece.move_lshape(cur_pos, "WNW", 1, 2)
    piece.move_lshape(cur_pos, "WSW", 1, 2)
    piece.move_lshape(cur_pos, "SSW", 1, 2)
    piece.move_lshape(cur_pos, "SSE", 1, 2)
    piece.move_lshape(cur_pos, "ESE", 1, 2)
    piece.move_lshape(cur_pos, "ENE", 1, 2)
    piece.move_lshape(cur_pos, "NNE", 1, 2)


def pawn_test(piece):
    piece.color = "Black"
    piece.promote("h7", 8)
    piece.promote("h8", 8)
    piece.promote("a1", 8)
    piece.promote("a2", 8)
    piece.color = "White"
    piece.promote("h7", 8)
    piece.promote("h8", 8)
    piece.promote("a1", 8)
    piece.promote("a2", 8)


def main():
    piece = GenericPiece("Black", "9")
    print("Left or Right")
    piece.move_sideways("h7", "Left", 1)
    piece.move_sideways("h2", "Left", 6)
    piece.move_sideways("h4", "Left", 3)
    piece.move_sideways("a2", "Right", 1)
    piece.move_sideways("a4", "Right", -9)
    piece.move_sideways("a7", "Right", -5)
    print("Down or Up")
    piece.move_up_down("h7", "Up", 1)
    piece.move_up_down("h2", "Up", 6)
    piece.move_up_down("h4", "Up", 3)
    piece.move_up_down("a2", "Down", 1)
    piece.move_up_down("a4", "Down", -9)
    piece.move_up_down("a7", "Down", -5)
    print("Diagonal")
    piece.move_diagonal("a1", "NW", 7)
    piece.move_diagonal("h1", "NW", 7)
    piece.move_diagonal("a1", "NE", 3)
    piece.move_diagonal("h8", "NE", 1)
    # finish testing for SE and SW
    print("South")
    piece.move_diagonal("a8", "SE", 7)
    piece.move_diagonal("h8", "SE", 7)
    piece.move_diagonal("h8", "SW", 3)
    piece.move_diagonal("h1", "SW", 1)
    print("Horsey Time")
    cur_pos = "c5"
    knight_test(piece, cur_pos)
    print("Edge Case 1")
    cur_pos = "a1"
    knight_test(piece, cur_pos)
    print("Test Pawn Promotion")
    pawn_test(piece)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()