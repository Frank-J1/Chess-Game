class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def get_legal_moves(self, board):
        raise NotImplementedError("This has yet to be implemented")
