# pieces/pawn.py
from pieces.piece import Piece

MAX_Y = 8
MAX_X = 8

class Pawn(Piece):
    def get_legal_moves(self, board):
        moves = []
        x, y = self.position

        if y + 1 < MAX_Y:
            moves.append((x, y + 1))

        if x - 1 >= 0 and y + 1 < MAX_Y:
            moves.append((x - 1, y + 1))

        if x + 1 < MAX_X and y + 1 < MAX_Y:
            moves.append((x + 1, y + 1))

        return moves
