# Global variables:

game_still_going = True

winner = None

current_player = 'X'

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']


def display_board():
    print(board[0] + ' | ', board[1] + ' | ', board[2])
    print(board[3] + ' | ', board[4] + ' | ', board[5])
    print(board[6] + ' | ', board[7] + ' | ', board[8])


def play_game():
    display_board()

    while game_still_going:
        handle_turn(current_player)

        check_game_over()

        flip_player()

    if winner == 'X' or winner == 'O':
        print(winner, ' wins!')

    if winner is None:
        print('Tie!')


def handle_turn(player):
    position = int(input('Choose a position from 1-9: ')) - 1

    board[position] = 'X'

    display_board()


def check_game_over():
    check_win()
    check_tie()


def check_win():
    return


def check_tie():
    return


def flip_player():
    return


play_game()
