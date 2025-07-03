from board import Board

def main():
    board = Board()
    board.print_board()

    move_string = input("Enter your move (e.g., 'e2 e4'): ")
    coords = board.parse_coordinates(move_string)
    print(coords)

if __name__ == "__main__":
    main()
