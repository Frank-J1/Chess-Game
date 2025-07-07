# pieces/pawn.py
from pieces.piece import Piece

MAX_Y = 8
MAX_X = 8

class Pawn(Piece):
    def symbol(self):
        return "P" if self.color == "white" else "p"
    
    def get_legal_moves(self, board):
        moves = []
        direction = -1 if self.color == "white" else 1
        x, y = self.position

        if board.grid[y + direction][x] is None:
            moves.append((x, y + direction))

            start_row = 6 if self.color == "white" else 1
            if y == start_row and board.grid[y + 2 * direction][x] is None:
                moves.append((x, y + 2 * direction))

        return moves