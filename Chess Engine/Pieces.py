from GenericPiece import GenericPiece


class KingPiece(GenericPiece):
    def __init__(self, color):
        super().__init_(color, float('inf'))
        self.name = "King"

    def move_rank(self, current_position, direction):
        super().move_sideways(current_position, direction, number_of_spaces=1)

    def move_file(self, current_position, direction):
        super().move_up_down(current_position, direction, number_of_spaces=1)

    def move_diagonal(self, current_position, direction):
        super().move_diagonal(current_position, direction, number_of_spaces=1)


class QueenPiece(GenericPiece):
    def __init__(self, color):
        super().__init__(color, 9)
        self.name = "Queen"

    def move_rank(self, current_position, direction, number_of_spaces):
        super().move_sideways(current_position, direction, number_of_spaces)

    def move_file(self, current_position, direction, number_of_spaces):
        super().move_up_down(current_position, direction, number_of_spaces)

    def move_diagonal(self, current_position, direction, number_of_spaces):
        super().move_diagonal(current_position, direction, number_of_spaces)


class RookPiece(GenericPiece):
    def __init__(self, color):
        super().__init__(color, 5)
        self.name = "Rook"

    def move_rank(self, current_position, direction, number_of_spaces):
        super().move_sideways(current_position, direction, number_of_spaces)

    def move_file(self, current_position, direction, number_of_spaces):
        super().move_up_down(current_position, direction, number_of_spaces)


class BishopPiece(GenericPiece):
    def __init__(self, color):
        super().__init__(color, 3)
        self.name = "Bishop"

    def move_diagonal(self, current_position, direction, number_of_spaces):
        super().move_diagonal(current_position, direction, number_of_spaces)


class KnightPiece(GenericPiece):
    def __init__(self, color):
        super().__init__(color, 3)
        self.name = "Knight"

    def move_horsey(self, current_position, direction):
        super().move_lshape(self, current_position, direction, number_of_file_spaces=1, number_of_rank_spaces=2)