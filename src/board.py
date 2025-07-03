from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King
from pieces.knight import Knight

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

        self.grid[7][1] = Knight("white", (1, 7))
        self.grid[7][6] = Knight("white", (6, 7))
        self.grid[0][1] = Knight("black", (1, 0))
        self.grid[0][6] = Knight("black", (6, 0))


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
                elif piece.__class__.__name__=="Knight":
                    row_str +="N " if piece.color == "white" else "n "
                else:
                    row_str += "ERROR "
            print(row_str)

    def parse_coordinates(self, move_str):
        parts = move_str.split()

        if len(parts) != 2:
            print("that is an invalid input!")
            return None
        start, end = parts

        try:
            x1 = ord(start[0]) - ord('a')
            y1 = 8 - int(start[1]) - 1

            x2 = ord(end[0]) - ord('a')
            y2 = 8 - int(end[1]) - 1

            return (x1, y1), (x2, y2)
        
        except:
            print ("invalid input!")
            return None

    def move_piece (self, start_pos, end_pos):
        x1, y1 = start_pos
        x2, y2 = end_pos

        piece = self.grid[y1][x1]

        legal_moves = piece.get_legal_moves(self)

        if (x2, y2) not in legal_moves:
            print("Not a valid move!")
            return False
        
        self.grid[y1][x1] = None
        self.grid[y2][x2] = piece
        piece.position = (x2, y2)

        return True