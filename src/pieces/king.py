from pieces.piece import Piece

class King(Piece):
    def symbol(self):
        return "K" if self.color == "white" else "k "
    
    def get_legal_moves(self, board):
        MAX_X = 8
        MAX_Y = 8

        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        x, y = self.position

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < MAX_X and 0 <= new_y < MAX_Y:
                moves.append((x, y))

        return moves