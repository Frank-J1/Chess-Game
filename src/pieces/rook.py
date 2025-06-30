from pieces.piece import Piece

MAX_Y = 8
MAX_X = 8

class Rook(Piece):
    def symbol(self):
        return "R" if self.color == "white" else "r"

    def get_legal_moves(self, board):
        moves = []
        x, y = self.position

        for dy in range (y + 1, MAX_Y):
            moves.append((x, dy))

        for dy in range (y - 1, -1, -1):
            moves.append((x, dy))

        for dx in range (x + 1, MAX_X):
            moves.append((dx, y))

        for dx in range (x - 1, -1, -1):
            moves.append((dx, y))

        return moves
