"""
Tic Tac Toe Player
"""

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
    xCounter = 0
    oCounter = 0
    
    xCounter = sum(row.count(X) for row in board)
    oCounter = sum(row.count(O) for row in board)
    
    if xCounter <= oCounter:
        return X
    else:
        return O
        
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                possibleActions.add((i,j))
    
    return possibleActions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action

    if board[i][j] is not EMPTY:
        raise ValueError


    newBoard = [row.copy() for row in board]  # Create a copy of the board
    newBoard[i][j] = player(board)  # Apply the action
    

    return newBoard 


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY:
            return board[i][0]
    
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not EMPTY:
            return board[0][j]
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]
    
    return None
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    
    else: 
        if all(board[i][j] is not EMPTY for i in range(3) for j in range (3)):
            return True 
        
        return False
    

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    
    elif winner(board) == O:
        return -1
    
    else:
        return 0 


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board) is True:
        return None
    
    
    currentPlayer = player(board)

    def max_value(board):
        if terminal(board):
            return utility(board)
        v = -math.inf 
        bestAction = None
        for action in actions(board):
            minimumValue = min_value(result(board, action))
            if minimumValue > v:
                v = minimumValue
                bestAction = action
        return v, bestAction
    
    def min_value(board):
        if terminal(board):
            return utility(board)
        v = math.inf
        bestAction = None 
        for action in actions(board):
            maximumValue = max_value(result(board,action))
            if maximumValue < v:
                v = maximumValue
                bestAction = action
        return v, bestAction
    
    if currentPlayer == X:
        action = max_value(board)
    
    elif currentPlayer == O:
        action = min_value(board)
    
    print(action)

    return action

