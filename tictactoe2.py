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

    if i < 0 or i > 2 or j < 0 or j > 2:
        raise ValueError

    if (board[i][j] == None):
        newBoard[i][j] = currentPlayer
    else:
        raise ValueError

    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check for horizontal win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]

    # Check for vertical win
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not None:
            return board[0][j]

    # Check for diagonal win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]

    if board[2][0] == board[1][1] == board[0][2] and board[2][0] is not None:
        return board[2][0]

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

    current_player = player(board)

    if current_player == X:
        best_val = -float('inf')
        alpha = -float('inf')
        beta = float('inf')
        best_move = None
        for action in actions(board):
            value = minimax_value(result(board, action), False, alpha, beta)
            if value > best_val:
                best_val = value
                best_move = action
            alpha = max(alpha, best_val)
        return best_move
    else:
        best_val = float('inf')
        alpha = -float('inf')
        beta = float('inf')
        best_move = None
        for action in actions(board):
            value = minimax_value(result(board, action), True, alpha, beta)
            if value < best_val:
                best_val = value
                best_move = action
            beta = min(beta, best_val)
        return best_move


def minimax_value(board, maximizer_turn, alpha, beta):
    if terminal(board):
        return utility(board)

    if maximizer_turn:
        value = -float('inf')
        for action in actions(board):
            value = max(value, minimax_value(result(board, action), False, alpha, beta))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for action in actions(board):
            value = min(value, minimax_value(result(board, action), True, alpha, beta))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value