from GenericMoves import GenericMoves
from PieceMoveList import PieceMoveList


def knight_test(piece, cur_pos, moves, pos):
    piece.move_lshape(cur_pos, "NNW", 1, 2)
    piece.move_lshape(cur_pos, "WNW", 1, 2)
    piece.move_lshape(cur_pos, "WSW", 1, 2)
    piece.move_lshape(cur_pos, "SSW", 1, 2)
    piece.move_lshape(cur_pos, "SSE", 1, 2)
    piece.move_lshape(cur_pos, "ESE", 1, 2)
    piece.move_lshape(cur_pos, "ENE", 1, 2)
    piece.move_lshape(cur_pos, "NNE", 1, 2)
    list = moves.l_move_list(pos)
    print(list)


def rook_test(piece, cur_pos, moves, pos):
    print("Horizontal Test")
    list_moves = [piece.move_sideways(cur_pos, "left", i) for i in range(1,8)]
    print(list_moves)
    list_moves = [piece.move_sideways(cur_pos, "right", i) for i in range(1,8)]
    print(list_moves)
    list = moves.horizontal_move_list(pos)
    print(list)
    print("Vertical Test")
    list_moves = [piece.move_up_down(cur_pos, "up", i) for i in range(1,8)]
    print(list_moves)
    list_moves = [piece.move_up_down(cur_pos, "down", i) for i in range(1, 8)]
    print(list_moves)
    list = moves.vertical_move_list(pos)
    print(list)

def main():
    piece = GenericMoves("Black", "9")
    knight = PieceMoveList(8, 8, 1, 2)
    print("Horsey Time")
    cur_pos = "c5"
    knight_test(piece, cur_pos, knight, [3,5])
    print("Edge Case 1")
    cur_pos = "a1"
    knight_test(piece, cur_pos, knight, [1,1])
    print("Rook Time")
    cur_pos = "c5"
    rook_test(piece, cur_pos, knight, [3, 5])
    cur_pos = "a1"
    rook_test(piece, cur_pos, knight, [1, 1])


# Using the special variable
# __name__
if __name__ == "__main__":
    main()