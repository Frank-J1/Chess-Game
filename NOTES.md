# Chess Game Project – Design Notes

## 🎯 Game Definition

- Full chess rules will be supported (castling, promotions, en passant, etc.)
- The game will be local multiplayer (two players on one device)
- A GUI will be used (likely with Pygame)
- A move history tracker will log all played moves

---

## 🧱 Main Components (Object-Oriented Design)

### Piece (Base Class)
- Each chess piece inherits from a common superclass `Piece`
- Responsibilities:
  - Store color (`white` or `black`)
  - Store current position (`(row, col)`)
  - Store type (e.g. "Pawn", "Knight")
  - Define method to return legal moves

### Subclasses
- `Pawn`, `Rook`, `Knight`, `Bishop`, `Queen`, `King` will override the legal move logic

### Board
- 8×8 grid represented by a 2D list
- Tiles will correspond to names like `e6`, `f1`, `h3`
- Will initialize with pieces in starting positions
- Will handle move validation, collision detection, and tile conversion (e.g., `(6, 4)` ↔ `'e2'`)

### Move
- Stores move history
- Validates legality of moves
- Tracks special moves (castling, promotion, etc.)
- May support undo

---

## 💾 Data Representation

- The board will be a list of lists: `board[row][col]` → `Piece` or `None`
- Each `Piece` will track its own position (`self.position = (row, col)`)
- We’ll convert between coordinates and algebraic notation for GUI readability

---

## 🖥️ GUI Plan (Pygame)

- Render the chessboard and pieces using Pygame
- Handle click input for piece selection and moves
- Highlight legal moves and game status
- Display current turn, check/checkmate messages, etc.

---

## ✅ Project Goals
- Practice OOP principles
- Build a playable chess game with full rules
- Implement a functional GUI
- (Optional) Add basic AI in the future (minimax)
