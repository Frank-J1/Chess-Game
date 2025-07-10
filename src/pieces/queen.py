from pieces.piece import Piece

class Queen(Piece):
    def symbol(self):
        return "Q" if self.color == "white" else "q"
    
    def get_legal_moves(self, board):
        #Diagonal
        MAX_X = 8
        MAX_Y = 8
        moves = []
        x, y = self.position
        for dx, dy in [(1,1), (1,-1), (-1, 1), (-1,-1)]:
            new_x, new_y = x + dx, y + dy

            while 0 <= new_x < MAX_X and 0 <= new_y < MAX_Y:
                if board.grid[new_x][new_y] == None:
                    moves.append((new_x, new_y))
                    new_x += dx
                    new_y += dy
                else:
                    break
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + dx, y + dy

            while 0 <= new_x < MAX_X and 0 <= new_y < MAX_Y:
                if board.grid[new_x][new_y] == None:
                    moves.append((new_x, new_y))
                    new_x += dx
                    new_y += dy
                else:
                    break

        return moves