"""
Tic Tac Toe Player
"""

import math
import copy

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
    if (board[0].count(None)+board[1].count(None)+board[2].count(None)) % 2 == 0:
        return O
    else:
        return X
    
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                actions.add((i,j))
    return actions
            
    
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = copy.deepcopy(board)
    
    if action not in actions(board):
        raise ValueError
    else:
        i, j = action
        board_copy[i][j] = player(board)
    return board_copy
        
    raise NotImplementedError

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0] == [X,X,X] or board[1] == [X,X,X] or board[2] == [X,X,X] or (board[0][0] == X and board[1][0] == X and board[2][0] == X) or (board[0][1] == X and board[1][1] == X and board[2][1] == X) or (board[0][2] == X and board[1][2] == X and board[2][2] == X) or (board[0][0] == X and board[1][1] == X and board[2][2] == X) or (board[0][2] == X and board[1][1] == X and board[2][0] == X):
        return X
    
    elif board[0] == [O,O,O] or board[1] == [O,O,O] or board[2] == [O,O,O] or (board[0][0] == O and board[1][0] == O and board[2][0] == O) or (board[0][1] == O and board[1][1] == O and board[2][1] == O) or (board[0][2] == O and board[1][2] == O and board[2][2] == O) or (board[0][0] == O and board[1][1] == O and board[2][2] == O) or (board[0][2] == O and board[1][1] == O and board[2][0] == O):
        return O
    else:
        return None
    
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == None and  (board[0].count(None)+board[1].count(None)+board[2].count(None)) > 0:
        return False
    else:
        return True
        
    raise NotImplementedError


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
    
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board): 
        return None
    
    #dict for choose best action
    score_per_action = {}
    
    if player(board) == X:
        for action in actions(board):
            score_per_action[action] = min_value(result(board, action))
        return max(score_per_action, key = score_per_action.get)
    else:
        for action in actions(board):
            score_per_action[action] = max_value(result(board, action)) 
        return min(score_per_action, key = score_per_action.get) 
        
    raise NotImplementedError
    
def max_value(board):
    if terminal(board):
        return utility(board)
    v = - 100
    for action in actions(board):
        v = max(v, min_value(result(board, action)))   
    return v
 
def min_value(board):
    if terminal(board):
        return utility(board)
    v = 100
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v   
    
