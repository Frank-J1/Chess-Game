class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def get_legal_moves(self, board):
        raise NotImplementedError("This has yet to be implemented")

class Pawn(Piece):
    def get_legal_moves(self, board):
        x, y = self.position
        moves = []

        if y + 1 < 8:
            moves.append((x, y + 1))
        if x > 0 and y + 1 < 8:
            moves.append((x - 1, y + 1))
        if x < 7 and y + 1 < 8:
            moves.append((x + 1, y + 1))

        return moves
