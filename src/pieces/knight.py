from pieces.piece import Piece

class Knight(Piece):

    def symbol(self):
        return "N" if self.color == "white" else "n"
    
    def get_legal_moves(self, board):
        x, y = self.position

        MAX_X = 8
        MAX_Y = 8
        directions =  [(2, 1), (1, 2), (-1, 2), (-2, 1),(-2, -1), (-1, -2), (1, -2), (2, -1)]
        moves = []

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < MAX_X and 0 <= new_y < MAX_Y:
                moves.append((new_x, new_y))

        return moves