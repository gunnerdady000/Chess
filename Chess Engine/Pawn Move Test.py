from PieceMoves import PawnMoves


def main():
    white_pawn = PawnMoves("White", "g2")
    black_pawn = PawnMoves("Black", "e7")
    w_cur_pos = "g2"
    b_cur_pos = "e7"
    print("Starting Positions")
    white_pawn.move_two_ranks(w_cur_pos)
    black_pawn.move_two_ranks(b_cur_pos)
    w_cur_pos = "g4"
    b_cur_pos = "e5"
    print("Already moved")
    white_pawn.move_two_ranks(w_cur_pos)
    black_pawn.move_two_ranks(b_cur_pos)
    print("Move single space")
    white_pawn.move_rank(w_cur_pos)
    black_pawn.move_rank(b_cur_pos)
    print("Test promotion Good")
    white_pawn.promote("g8")
    black_pawn.promote("e1")
    print("Test promotion Bad")
    white_pawn.promote("g1")
    black_pawn.promote("e8")
    print("Attack diagonal")
    w_cur_pos = "f5"
    b_cur_pos = "g6"
    print("Good direction")
    white_pawn.move_diagonal(w_cur_pos, "NW")
    white_pawn.move_diagonal(w_cur_pos, "NE")
    black_pawn.move_diagonal(b_cur_pos, "SW")
    black_pawn.move_diagonal(b_cur_pos, "SE")
    print("Bad direction")
    white_pawn.move_diagonal(w_cur_pos, "SW")
    white_pawn.move_diagonal(w_cur_pos, "SE")
    black_pawn.move_diagonal(b_cur_pos, "NW")
    black_pawn.move_diagonal(b_cur_pos, "NE")


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
