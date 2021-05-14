on_board = {
    '9' : ' ',
    '8' : ' ',
    '7' : ' ',
    '6' : ' ',
    '5' : ' ',
    '4' : ' ',
    '3' : ' ',
    '2' : ' ',
    '1' : ' '
}

def Board(lable):
    print(lable['7'] + ' | ' + lable['8'] + ' | ' + lable['9'])
    print('..+...+..')
    print(lable['4'] + ' | ' + lable['5'] + ' | ' + lable['6'])
    print('..+...+..')
    print(lable['1'] + ' | ' + lable['2'] + ' | ' + lable['3'])
    print('..+...+..')

turn = 'X'
count = 0

while True:
    print(turn,'turn')
    
    Board(on_board)

    move = input('Enter the place number: ')

    if on_board[move] == ' ':
        on_board[move] = turn
        count += 1
    else:
        print('The place is already filled')
        continue

    if count>=5:
        if on_board['7'] == on_board['8'] == on_board['9'] != ' ':
            Board(on_board)
            print("\nGame Over.\n")                
            print(turn + " WON.")             
            break
        elif on_board['4'] == on_board['5'] == on_board['6'] != ' ':
            Board(on_board)
            print("\nGame Over.\n")                
            print(turn + " WON.")                
            break
        elif on_board['1'] == on_board['2'] == on_board['3'] != ' ':
            Board(on_board)
            print("\nGame Over.\n")                
            print(turn + " WON.")                
            break
        elif on_board['7'] == on_board['4'] == on_board['1'] != ' ':
            Board(on_board)
            print("\nGame Over.\n")                
            print(turn + " WON.")                
            break
        elif on_board['8'] == on_board['5'] == on_board['2'] != ' ':
            Board(on_board)
            print("\nGame Over.\n")                
            print(turn + " WON.")                
            break
        elif on_board['9'] == on_board['6'] == on_board['3'] != ' ':
            Board(on_board)
            print("\nGame Over.\n")                
            print(turn + " WON.")                
            break
        elif on_board['7'] == on_board['5'] == on_board['3'] != ' ':
            Board(on_board)
            print("\nGame Over.\n")                
            print(turn + " WON.")                
            break
        elif on_board['9'] == on_board['5'] == on_board['1'] != ' ':
            Board(on_board)
            print("\nGame Over.\n")                
            print(turn + " WON.")                
            break
        
    if count >= 9:
        print('Match is Draw')
        break
    
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

    print('\n')