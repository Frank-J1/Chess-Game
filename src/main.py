from Piece import Pawn

print("Hello from main.py!")  # Step 1: Confirm script runs at all

from Piece import Pawn

pawn = Pawn("white", (3, 3))
moves = pawn.get_legal_moves(None)

print("Legal moves for Pawn at (3, 3):", moves)
