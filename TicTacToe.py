
def boardprint(placements):
    print('_________')
    print(f"{placements[0][0]}|{placements[0][1]}|{placements[0][2]}")
    print('-----')
    print(f"{placements[1][0]}|{placements[1][1]}|{placements[1][2]}")
    print('-----')
    print(f"{placements[2][0]}|{placements[2][1]}|{placements[2][2]}")
    print('_________')

def checkTurn(turnTest):



    if turnTest %2 == 0:
        return('X')
    else: return('O')



def get_place():
    while(True):
        Row = input('enter row:')
        Column = input('enter column:')
        if (Row >='1' and Row <='3' and Column >='1' and Column <='3'): return int(Row) - 1 , int (Column) - 1
        else:
            print('Incorrect parameters for lines, they should be between 1 -> 3')

def game_over(placements):
    for i in range(3):
        if placements[i][0] == placements[i][1] and placements[i][0] == placements[i][2] and placements[i][0] != ' ':
            return False
    for i in range(3):
        if placements[0][i] == placements[1][i] and placements[0][i] == placements[2][i] and placements[0][i] != ' ':
            return False
    if placements[0][0] == placements[1][1] and placements[0][0] == placements[2][2] and placements[0][0] != ' ':
        return False
    if placements[2][0] == placements[1][1] and placements[2][0] == placements[0][2] and placements[2][0] != ' ':
        return False

    return True

PlayAgain = 'y'
while PlayAgain == 'y':
    board = [[' ', ' ', ' '],  [' ', ' ', ' '] ,[' ', ' ', ' ']]
    turn = 0
    boardprint(board)

    while turn<=8 and game_over(board):
        print(f"{checkTurn(turn)} turn!")
        Row, Column = get_place()
        if board[Row][Column] == ' ':
            board[Row][Column] = checkTurn(turn)
            turn += 1
            boardprint(board)
        else:
            print('there is already someone on this spot!')

    print('Game Over!')
    if turn == 9: print('Its a Tie!')
    elif turn % 2 == 0: print('O Wins!')
    elif turn % 2 == 1: print ('X Wins!')
    PlayAgain = input('play again? - y/n: ')