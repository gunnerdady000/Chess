from GenericMoves import GenericMoves


class KingMoves(GenericMoves):
    def __init__(self, color):
        super().__init_(color, float('inf'))
        self.name = "King"

    def move_rank(self, current_position, direction):
        super().move_sideways(current_position, direction, number_of_spaces=1)

    def move_file(self, current_position, direction):
        super().move_up_down(current_position, direction, number_of_spaces=1)

    def move_diagonal(self, current_position, direction):
        super().move_diagonal(current_position, direction, number_of_spaces=1)


class QueenMoves(GenericMoves):
    def __init__(self, color):
        super().__init__(color, 9)
        self.name = "Queen"

    def move_file(self, current_position, direction, number_of_spaces):
        super().move_sideways(current_position, direction, number_of_spaces)

    def move_rank(self, current_position, direction, number_of_spaces):
        super().move_up_down(current_position, direction, number_of_spaces)

    def move_diagonal(self, current_position, direction, number_of_spaces):
        super().move_diagonal(current_position, direction, number_of_spaces)


class RookMoves(GenericMoves):
    def __init__(self, color):
        super().__init__(color, 5)
        self.name = "Rook"

    def move_file(self, current_position, direction, number_of_spaces):
        super().move_sideways(current_position, direction, number_of_spaces)

    def move_rank(self, current_position, direction, number_of_spaces):
        super().move_up_down(current_position, direction, number_of_spaces)


class BishopMoves(GenericMoves):
    def __init__(self, color):
        super().__init__(color, 3)
        self.name = "Bishop"

    def move_diagonal(self, current_position, direction, number_of_spaces):
        super().move_diagonal(current_position, direction, number_of_spaces)


class KnightMoves(GenericMoves):
    def __init__(self, color):
        super().__init__(color, 3)
        self.name = "Knight"

    def move_horsey(self, current_position, direction):
        super().move_lshape(self, current_position, direction, number_of_file_spaces=1, number_of_rank_spaces=2)


class PawnMoves(GenericMoves):
    def __init__(self, color, starting_position):
        super().__init__(color, 1)
        self.name = "Pawn"
        self.starting_position = starting_position

    def move_two_ranks(self, current_position):
        if current_position == self.starting_position:
            if self.color.lower() == "white":
                super().move_up_down(current_position, "Up", 2)
            elif self.color.lower() == "black":
                super().move_up_down(current_position, "Down", 2)
        else:
            print("Not in starting position")
            return

    def move_rank(self, current_position):
        if self.color.lower() == "white":
            super().move_up_down(current_position, "Up", 1)
        elif self.color.lower() == "black":
            super().move_up_down(current_position, "Down", 1)

    def promote(self, current_position):
        super().promote(current_position, number_of_ranks=8)

    def move_diagonal(self, current_position, direction):
        if self.color.lower() == "white":
            if direction.upper() == "NW" or direction.upper() == "NE":
                super().move_diagonal(current_position, direction, 1)
            else:
                print("Incorrect direction for color piece")
        elif self.color.lower() == "black":
            if direction.upper() == "SW" or direction.upper() == "SE":
                super().move_diagonal(current_position, direction, 1)
            else:
                print("Incorrect direction for color piece")

    def enpassant(self, current_position):
        # This is tricky. Or does this go into the engine?
        pass
