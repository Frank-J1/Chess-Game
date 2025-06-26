Chess game project:

DEFINING THE GAME:
- This will have every rule that chess has (ie: castle, promotions etc...)
- The game will be one player vs another player (not like an online version but on the same device)
- The game will be done through GUI 
- There should be a history tracker that keeps the moves that are being played

Main components:
- This will be done in a object oriented way;
	- Each chess peice will inherient from a super class called "peice"
	- Board will be a 8x8 grid with the tile names (ie e6, f1, h3 etc)
	- Move will have the move history, check if the move is legal etc...

Representation for data:
- The board can simply be a array with rows and coloums that holds the peice object
- TO know where each peice is on the board we will just check the position on the board (ie self.position (row, col)


The Board will:
- Store an 8x8 grid using a 2D list
- Initialize with all pieces in the correct positions
- Handle checking if a square is empty, has an opponent piece, etc.
- Convert between board indices and chess notation (like e4 ↔ (4, 4))

Each Piece will:
- Store its color (white/black)
- Store its current position (e.g., (0, 0) or 'a1')
- Implement a method to return its legal moves
- Know its type (Pawn, Rook, etc.) via class or name attribute

The GUI will:
- Visually render the board and pieces
- Highlight selected squares and legal moves
- Allow player to click/select pieces and move them
- Display game status (check, checkmate, turn, etc.)

The Move system will:
- Store a list of all moves made
- Track special moves like castling, promotion, en passant
