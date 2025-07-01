from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King

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

        self.grid[7][2] = Bishop("white", (2, 7))
        self.grid[7][5] = Bishop("white", (5, 7))
        self.grid[0][2] = Bishop("black", (2, 0))
        self.grid[0][5] = Bishop("black", (5, 0))

        self.grid[7][3] = Queen("white", (3, 7))
        self.grid[0][3] = Queen("black", (3, 0))

        self.grid[7][4] = King("white", (4, 7))
        self.grid[0][4] = King("black", (4, 0))


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
                elif piece.__class__.__name__=="Bishop":
                    row_str +="B " if piece.color == "white" else "b "
                elif piece.__class__.__name__=="Queen":
                    row_str +="Q " if piece.color == "white" else "q "
                elif piece.__class__.__name__=="King":
                    row_str +="K " if piece.color == "white" else "k "
                else:
                    row_str += "ERROR "
            print(row_str)
