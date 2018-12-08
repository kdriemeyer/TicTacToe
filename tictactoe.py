# Tic Tac Toe

import random
import copy


def drawBoard(board):
    # This function prints out the board that it was passed.

    # "board" is a list of lists representing the board

    print('   |   |')
    print(' ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2])


def inputPlayerLetter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the list is the player's letter, the second is the computer's letter.
    if letter == 'X':
        return['X', 'O']
    else:
        return['O', 'X']


def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns false.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def makeMove(b, letter, input_move):
    b[input_move[0]][input_move[1]] = letter


def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo for 'board' and le for 'letter'
    return (
        (bo[0][0] == le and bo[0][1] == le and bo[0][2] == le) or  # across the top
        (bo[1][0] == le and bo[1][1] == le and bo[1][2] == le) or  # across the middle
        (bo[2][0] == le and bo[2][1] == le and bo[2][2] == le) or  # across the bottom
        (bo[0][0] == le and bo[1][0] == le and bo[2][0] == le) or  # down the left side#
        (bo[0][1] == le and bo[1][1] == le and bo[2][1] == le) or  # down the middle
        (bo[0][2] == le and bo[1][2] == le and bo[2][2] == le) or  # down the right side
        (bo[0][0] == le and bo[1][1] == le and bo[2][2] == le) or  # diagonal 1
        (bo[0][2] == le and bo[1][1] == le and bo[2][0] == le))    # diagonal 2


def getBoardCopy(board):
    # Make a duplicate of the board list and return the duplicate

    dupe_board = copy.deepcopy(board)

    return dupe_board


def isSpaceFree(board, input_move):
    # Return true if the passed move is legal on the passed board
    return board[input_move[0]][input_move[1]] == ' '


def getPlayerMove(board):
    # Let the player type in their move
    row = -1
    col = -1

    while (row not in [0, 1, 2] and col not in [0, 1, 2]) or not isSpaceFree(board, [row, col]):
        print('What is your next move?')
        row = int(input('Enter row between 1 and 3')) - 1
        col = int(input('Enter column between 1 and 3')) - 1
        player_move = [row, col]

    return player_move


def chooseRandomMoveFromList(board, moves_list):
    # Returns a valid move from the passed list on the passed board
    # Returns None if there is no valid move
    possible_moves = []
    for i in moves_list:
        if isSpaceFree(board, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def getComputerMove(board, computer_letter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computer_letter == 'X':
        player_letter = '0'
    else:
        player_letter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for r in range(0, 3):
        for c in range(0, 3):
            board_copy = getBoardCopy(board)
            i = [r, c]
            if isSpaceFree(board_copy, i):
                makeMove(board_copy, computerLetter, i)
                if isWinner(board_copy, computerLetter):
                    return i

    # Check if the player could win on their next move, and block them.
    for r in range(0, 3):
        for c in range(0, 3):
            board_copy = getBoardCopy(board)
            i = [r, c]
            if isSpaceFree(board_copy, i):
                makeMove(board_copy, player_letter, i)
                if isWinner(board_copy, player_letter):
                    return i

    # Try to take one of the corners, if free
    comp_move = chooseRandomMoveFromList(board, [[0, 0], [0, 2], [2, 0], [2, 2]])
    if comp_move is not None:
        return comp_move

    # Try to take the center, if free
    if isSpaceFree(board, [1, 1]):
        return [1, 1]

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [[0, 1], [1, 0], [1, 2], [2, 1]])


def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return false.

    for r in range(0, 3):
        for c in range(0, 3):
            if isSpaceFree(board, [r, c]):
                return False
    return True


print('Welcome to Tic Tac Toe!')


while True:
    # Reset the board
    theBoard = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Player's turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! YOu won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        else:
            # Computer's turn
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer won! You lost.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break
