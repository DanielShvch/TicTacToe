
def boardprint(placements): # printing the board
    print('_________')
    print(f"{placements[0][0]}|{placements[0][1]}|{placements[0][2]}")
    print('-----')
    print(f"{placements[1][0]}|{placements[1][1]}|{placements[1][2]}")
    print('-----')
    print(f"{placements[2][0]}|{placements[2][1]}|{placements[2][2]}")
    print('_________')

def checkTurn(turnTest): # check whos turn it is
    if turnTest %2 == 0:
        return('X')
    else: return('O')



def get_place(): # ask user where to place his player, also if he gives incorrect parameters tell him.
    while(True):
        Row = input('enter row:')
        Column = input('enter column:')
        if (Row >='1' and Row <='3' and Column >='1' and Column <='3'): return int(Row) - 1 , int (Column) - 1
        else:
            print('Incorrect parameters for lines, they should be between 1 -> 3')

def game_over(placements):  # check for winning statements.
    for i in range(3): # if any Row is winning
        if placements[i][0] == placements[i][1] and placements[i][0] == placements[i][2] and placements[i][0] != ' ': # if any lines is winning
            return False
    for i in range(3):  #if any Column is winning
        if placements[0][i] == placements[1][i] and placements[0][i] == placements[2][i] and placements[0][i] != ' ':
            return False
    if placements[0][0] == placements[1][1] and placements[0][0] == placements[2][2] and placements[0][0] != ' ':
        return False = #if win by diagonal
    if placements[2][0] == placements[1][1] and placements[2][0] == placements[0][2] and placements[2][0] != ' ':
        return False #if win by backwards diagonal

    return True #if none of the above the game will continue

PlayAgain = 'y' #for looping the game infinitely until player decides not to
while PlayAgain == 'y':
    board = [[' ', ' ', ' '],  [' ', ' ', ' '] ,[' ', ' ', ' ']] #setting the board to blank
    turn = 0 # setting turn for X first
    boardprint(board) # go print the board

    while turn<=8 and game_over(board): # statement for if the game is over by winning or no spaces left
        print(f"{checkTurn(turn)} turn!") # tell which players turn it is
        Row, Column = get_place() # get place from user via function
        if board[Row][Column] == ' ': #if there is already some one in the spot it will tell the player to try again.
            board[Row][Column] = checkTurn(turn
            turn += 1
            boardprint(board)
        else:
            print('there is already someone on this spot!')

    print('Game Over!') #The EndGame
    if turn == 9: print('Its a Tie!')
    elif turn % 2 == 0: print('O Wins!')
    elif turn % 2 == 1: print ('X Wins!')
    PlayAgain = input('play again? - y/n: ' #prompt if the palyer want to play again