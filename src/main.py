from board import Board

def main():
    board = Board()
    board.print_board()

    move_string = input("Enter your move (e.g., 'e2 e4'): ")
    coords = board.parse_coordinates(move_string)
    print(coords)

    current_turn = "white"

    while True:
        move_string = input("Enter your move (e.g., 'e2 e4'): ")
        coords = board.parse_coordinates(move_string)

        if coords is None:
            print ("please enter a valid move.!")
            continue 
        
        start_pos, end_pos = coords

        if board.move_piece(start_pos, end_pos, current_turn):
            current_turn = "black" if current_turn == "white" else "white"

if __name__ == "__main__":
    main()
