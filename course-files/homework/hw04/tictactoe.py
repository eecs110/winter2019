def print_board(game_data):
    print()
    print('', game_data[6], '|', game_data[7], '|', game_data[8], '       7 | 8 | 9 ')
    print('-'* 11, '    ', '-'* 11)
    print('', game_data[3], '|', game_data[4], '|', game_data[5], '       4 | 5 | 6 ')
    print('-'* 11, '    ', '-'* 11)
    print('', game_data[0], '|', game_data[1], '|', game_data[2], '       1 | 2 | 3 ')
    print()


game_data = [' '] * 9   # initialize game data to an empty array
player_symbol = 'o'     # TODO: make this customizable
computer_symbol = 'x'   # TODO: make this customizable
whose_turn = 'player'   # TODO: alternate between computer and player

# keep looping until there's a winner:
while True:
    print_board(game_data)
    
    if whose_turn == 'player':
        selection = int(input('Where would you like to go (0-9)? '))
        game_data[selection - 1] = player_symbol