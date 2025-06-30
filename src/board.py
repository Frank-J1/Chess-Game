from pieces.pawn import Pawn
from pieces.rook import Rook

class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces()

    def setup_pieces(self):
        # Setup pawns
        for col in range(8):
            self.grid[6][col] = Pawn("white", (col, 6))
            self.grid[1][col] = Pawn("black", (col, 1))

        # Setup rooks
        self.grid[7][0] = Rook("white", (0, 7))
        self.grid[7][7] = Rook("white", (7, 7))
        self.grid[0][0] = Rook("black", (0, 0))
        self.grid[0][7] = Rook("black", (7, 0))


    def print_board(self):
        for row in self.grid:
            row_str = ""
            for piece in row:
                if piece is None:
                    row_str += ". "
                elif piece.__class__.__name__ =="Pawn":
                    row_str += "P " if piece.color == "white" else "p "
                elif piece.__class__.__name__ =="Rook":
                    row_str += "R " if piece.color == "white" else "r "
                else:
                    row_str += "ERROR "
            print(row_str)
