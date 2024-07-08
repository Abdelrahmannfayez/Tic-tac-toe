import mode_two
def print_board(board):
    print("""
             {} | {} | {}
            --------
             {} | {} | {}
            --------
             {} | {} | {}
           """.format(board[0][0], board[0][1], board[0][2],
                      board[1][0], board[1][1], board[1][2],
                      board[2][0], board[2][1], board[2][2]))

def intro():
    print("  _______ _        _______           _______          ")
    print(" |__   __(_)      |__   __|         |__   __|         ")
    print("    | |   _  ___     | | __ _  ___     | | ___   ___  ")
    print("    | |  | |/ __|    | |/ _` |/ __|    | |/ _ \\ / _ \\ ")
    print("    | |  | | (__     | | (_| | (__     | | (_) |  __/ ")
    print("    |_|  |_|\\___|    |_|\\__,_|\\___|    |_|\\___/ \\___| ")
    print("player 1: X")
    print("player 2: O")

def game():
    players = {1: 'X', 2: 'O'}
    m = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2)
    }
    arr = [
        ['', '', ''],
        ['', '', ''],
        ['', '', '']
    ]
    turn = 0
    win = 0

    print()
    print_board(arr)
    print()

    while True:
        # move
        pos = int(input(f"player {(turn % 2) + 1} turn:  "))
        if pos < 1 or pos > 9 or arr[m[pos][0]][m[pos][1]] in ['X', 'O']:
            print("Invalid move. Try again.")
            continue
        arr[m[pos][0]][m[pos][1]] = players[(turn % 2) + 1]
        # print
        print_board(arr)

        # check rows
        for i in range(3):
            if arr[i][0] == arr[i][1] == arr[i][2]:
                if arr[i][0] == 'X':
                    win = 1
                elif arr[i][0] == 'O':
                    win = 2
        # check cols
        for i in range(3):
            if arr[0][i] == arr[1][i] == arr[2][i]:
                if arr[0][i] == 'X':
                    win = 1
                elif arr[0][i] == 'O':
                    win = 2
        # check diagonals
        if arr[0][0] == arr[1][1] == arr[2][2]:
            if arr[0][0] == 'X':
                win = 1
            elif arr[0][0] == 'O':
                win = 2
        if arr[0][2] == arr[1][1] == arr[2][0]:
            if arr[0][2] == 'X':
                win = 1
            elif arr[0][2] == 'O':
                win = 2

        if win == 1:
            print("Player 1 Won !!")
            break
        if win == 2:
            print("Player 2 Won !!")
            break
        if turn == 8:
            print("\nTie!!")
            break

        turn += 1

if __name__ == "__main__":
    intro()
    mode=1
    while mode:
        print("mode 1 : 1 vs 1")
        print("mode 2 : 1 vs pc")
        mode = input("enter mode 1/2 or 0 to exit")
        if mode == "1":
            cont = 'Y'
            while cont.upper() == 'Y':
                game()
                cont = input("Continue 1 vs 1 ? ~Y ~N")
        elif mode=="2":
            cont="Y"
            while cont.upper() == 'Y':
                game_2 = mode_two.TicTacToe()
                game_2.play_game()
                cont = input("Continue 1 vs pc ? ~Y ~N")
        else:
            exit()


        