class GenericPiece:
    def __init__(self, color, piece_value):
        self.color = color
        self.piece_value = piece_value
        self.coordinate_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
        self.inverse_coordinate_dict = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h"}

    def move_sideways(self, current_position, direction, number_of_spaces):
        if direction.lower() == "left":
            spaces = 0 - abs(number_of_spaces)
        elif direction.lower() == "right":
            spaces = abs(number_of_spaces)
        else:
            print("Bad number of spaces or incorrect direction")
            return

        # move by number of spaces across the row
        updated_position = self.coordinate_dict[current_position[0]] + spaces

        # check to see if the updated position is past the boundary columns
        if self.check_boundary(updated_position):
            # return the updated strip position
            new_position = self.inverse_coordinate_dict[updated_position] + current_position[1]
            self.position_update(current_position, new_position)
        else:
            # place holder for return to engine
            print("Illegal Move")

    def move_up_down(self, current_position, direction, number_of_spaces):
        if direction.lower() == "down":
            spaces = 0 - abs(number_of_spaces)
        elif direction.lower() == "up":
            spaces = abs(number_of_spaces)
        else:
            print("Bad number of spaces or incorrect direction")
            return

        # move by number of updated spaces across the column
        updated_position = int(current_position[1]) + spaces

        # check to see if the updated position is past the boundary columns
        if self.check_boundary(updated_position):
            # return the updated strip position
            new_position = current_position[0] + str(updated_position)
            self.position_update(current_position, new_position)
        else:
            # place holder for return to engine
            print("Illegal Move")

    def diagonal(self, current_position, direction, number_of_spaces):
        # diagonal movement in the form of f(x) -> i+/-x, j+/-x
        # convert the current_position to int pair
        file = self.coordinate_dict[current_position[0]]
        rank = int(current_position[1])

        # directions in form of compass (NW, SW, NE, SE)
        if direction.lower() == "nw":
            # f(x) -> i-x, j+x
            updated_file = file - abs(number_of_spaces)
            # check bounds of updated file
            if not self.check_boundary(updated_file):
                print("Illegal Move")
                return
            updated_rank = rank + abs(number_of_spaces)
            # check bounds of updated rank
            if not self.check_boundary(updated_rank):
                print("Illegal Move")
                return
        elif direction.lower() == "sw":
            # f(x) -> i-x, j-x
            updated_file = file - abs(number_of_spaces)
            # check bounds of updated file
            if not self.check_boundary(updated_file):
                print("Illegal Move")
                return
            updated_rank = rank - abs(number_of_spaces)
            # check bounds of updated rank
            if not self.check_boundary(updated_rank):
                print("Illegal Move")
                return
        elif direction.lower() == "ne":
            # f(x) -> i+x, j+x
            updated_file = file + abs(number_of_spaces)
            # check bounds of updated file
            if not self.check_boundary(updated_file):
                print("Illegal Move")
                return
            updated_rank = rank + abs(number_of_spaces)
            # check bounds of updated rank
            if not self.check_boundary(updated_rank):
                print("Illegal Move")
                return
        elif direction.lower() == "se":
            # f(x) -> i+x, j-x
            updated_file = file - abs(number_of_spaces)
            # check bounds of updated file
            if not self.check_boundary(updated_file):
                print("Illegal Move")
                return
            updated_rank = rank + abs(number_of_spaces)
            # check bounds of updated rank
            if not self.check_boundary(updated_rank):
                print("Illegal Move")
                return
        else:
            print("Bad number of spaces or incorrect direction")
            return

        # convert rank and file to return new position
        new_position = self.inverse_coordinate_dict[updated_file] + str(updated_rank)
        self.position_update(current_position, new_position)

    @staticmethod
    def check_boundary(updated_position):
        # check to see if the updated position is past boundary column or row
        if updated_position < 1:
            # past the A column / 1 row, return False that the move is illegal
            return False
        elif updated_position > 8:
            # past the H column / 8 row, return False that the move is illegal
            return False
        else:
            return True

    @staticmethod
    def position_update(current_position, new_position):
        print(current_position + " to " + new_position)


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
    piece.diagonal("a1", "NW", 7)
    piece.diagonal("h1", "NW", 7)
    piece.diagonal("a1", "NE", 3)
    piece.diagonal("h8", "NE", 1)
    # finish testing for SE and SW


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
