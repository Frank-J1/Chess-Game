from pieces.piece import Piece


MAX_Y = 8
MAX_X = 8

class Bishop(Piece):
    def symbol(self):
        return "B" if self.color == "white" else "b"
    
    def get_legal_moves(self, board):
        moves = []
        x, y = self.position

        directions = [(1,1), (1,-1), (-1, 1), (-1,-1)]

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            while 0 <= new_x < MAX_X and 0 <= new_y < MAX_Y:
                moves.append((new_x, new_y))
                new_x += dx
                new_y += dy

        return moves