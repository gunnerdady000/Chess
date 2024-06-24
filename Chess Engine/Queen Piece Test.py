from Pieces import QueenPiece

def main():
    piece = QueenPiece("Black")
    print("Left or Right")
    piece.move_rank("h7", "Left", 1)
    piece.move_rank("h2", "Left", 6)
    piece.move_rank("h4", "Left", 3)
    piece.move_rank("a2", "Right", 1)
    piece.move_rank("a4", "Right", -9)
    piece.move_rank("a7", "Right", -5)
    print("Down or Up")
    piece.move_file("h7", "Up", 1)
    piece.move_file("h2", "Up", 6)
    piece.move_file("h4", "Up", 3)
    piece.move_file("a2", "Down", 1)
    piece.move_file("a4", "Down", -9)
    piece.move_file("a7", "Down", -5)
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
    print(piece.piece_value)
    print(piece.name)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()