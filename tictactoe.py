"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    XCount = 0
    OCount = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                XCount += 1
            elif board[i][j] == 'O':
                OCount += 1
    if XCount == OCount:
        return 'X'
    return 'O'





def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    options = set()

    for i in range(3):
        for j in range(3):
            if (board[i][j] == None):
                options.add((i,j))

    return options



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]
    newBoard = copy.deepcopy(board)
    currentPlayer = player(board)

    if (board[i][j] == None):
        newBoard[i][j] = currentPlayer
    else:
        raise Exception

    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check for horizontal win
    for i in range(3):
        element = board[i][0]
        count = 1
        for j in range(1,3):
            if board[i][j] == element:
                count += 1
        if count == 3:
            return element

    # Check for vertical win
    for j in range(3):
        element = board[0][j]
        count = 1
        for i in range(1,3):
            if board[i][j] == element:
                count += 1
        if count == 3:
            return element

    # Check for diagonal win
    element = board[0][0]
    count = 1

    for i in range(1,3):
        if board[i][i] == element:
            count += 1
    if count == 3:
        return element

    element = board[2][0]
    count = 1

    for i in range(1,-1,-1):
        if board[i][2-i] == element:
            count += 1
    if count == 3:
        return element

    # If no winner, return None
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) != None):
        return True

    emptyCount = 0

    for i in range(3):
        for j in range(3):
            if (board[i][j] == None):
                emptyCount += 1
    if emptyCount == 0:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == 'X':
        return 1
    if winner(board) == 'O':
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    possibleActions = actions(board)

    if player(board) == X:

        maxVal = -float('inf')
        count = 0
        for action in possibleActions:
            if count == 0:
                firstActionScore = minimaxHelper(result(board,action), False)
                if firstActionScore > maxVal:
                    maxVal = firstActionScore
                    optimalMove = action
            else:
                actionScore = minimaxHelper2(result(board,action), False, firstActionScore)
                if actionScore == None:
                    continue
                if actionScore > maxVal:
                    maxVal = actionScore
                    optimalMove = action

            count+=1

    else:
        minVal = float('inf')

        count = 0
        for action in possibleActions:
            if (count == 0):
                firstActionScore = minimaxHelper(result(board, action), True)
                if firstActionScore < minVal:
                    minVal = firstActionScore
                    optimalMove = action
            else:
                actionScore = minimaxHelper2(result(board, action), True, firstActionScore)
                if actionScore == None:
                    continue
                if actionScore < minVal:
                    minVal = actionScore
                    optimalMove = action
            count += 1
    return optimalMove




def minimaxHelper(board, maximizerTurn):
    if terminal(board):
        return utility(board)

    if maximizerTurn == True:
        maxVal = -float('inf')
        possibleActions = actions(board)
        for action in possibleActions:
            actionScore = minimaxHelper(result(board, action), False)

            maxVal = max(actionScore, maxVal)

        return maxVal

    else:
        minVal = float('inf')
        possibleActions = actions(board)
        for action in possibleActions:
            actionScore = minimaxHelper(result(board, action), True)

            minVal = min(actionScore, minVal)
        return minVal


def minimaxHelper2(board, maximizerTurn, compVal):
    if terminal(board):
        return utility(board)

    if maximizerTurn == True:
        maxVal = -float('inf')
        possibleActions = actions(board)
        for action in possibleActions:
            actionScore = minimaxHelper(result(board, action), False)
            if actionScore > compVal:
                return None

            maxVal = max(actionScore, maxVal)

        return maxVal

    else:
        minVal = float('inf')
        possibleActions = actions(board)
        for action in possibleActions:
            actionScore = minimaxHelper(result(board, action), True)

            if actionScore < compVal:
                return None

            minVal = min(actionScore, minVal)
        return minVal
