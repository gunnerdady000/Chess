class Pawn:
    def __init__(self, color):
        # assign pawn piece color
        self.color = color
        self.initial_position = True

    def move_forward(self, current_position):
        # if initial position then can move 2 spaces forward else
        if not self.initial_position:
            # update position by one space
            updated_position = current_position[0] + self.update_chararcter(current_position[1], 1)
            print(current_position + " to " + updated_position)
            if self.promote(updated_position):
                print("Change me")
        else:
            # update position by 2 squares
            updated_position = current_position[0] + self.update_chararcter(current_position[1], 2)
            print(current_position + " to " + updated_position)
            self.initial_position = False

    def attack(self, current_position):
        # attacks diagonally

        # maybe remove board position check for the board?
        # check if not on the edge of board
        if not "a" in current_position and not "h" in current_position:
            # print("In the middle")
            # select the left or right position to attack
            future_position_left = None
            future_position_right = None
        elif "a" in current_position:
            # print("On Left side of board")
            future_position_right = None
        elif "h" in current_position:
            # print("On Right side of board")
            future_position_left = None
        else:
            print("Error")

    # promote pawn
    def promote(self, current_position):
        # if entering Row 8 as white, or Row 1 as Black, promote piece
        if self.color == "White" and current_position[1] == "8":
            print("Select Promoted White Piece")
        elif self.color == "Black" and current_position[1] == "1":
            print("Select Promoted Black Piece")
        else:
            print("Promotion Error")
        return True

    def enpassant(self):
        # weird pawn trick

        None

    def update_chararcter(self, character, value):
        # update the char by adding a value
        if self.color == "White":
            updated_position = chr(ord(character) + value)
        elif self.color == "Black":
            updated_position = chr(ord(character) - value)
        else:
            print("Pawn update character error")

        return updated_position

def main():
    piece = Pawn("Black")
    piece.move_forward("h7")
    piece.move_forward("h2")
    piece.move_forward("h4")
    piece.move_forward("a2")
    piece.move_forward("a4")
    piece.move_forward("a7")
    piece = Pawn("White")
    piece.move_forward("h2")
    piece.move_forward("h4")
    piece.move_forward("h7")
    piece.move_forward("a2")
    piece.move_forward("a4")
    piece.move_forward("a7")


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
