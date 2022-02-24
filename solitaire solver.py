#Soltaire peg game solver
board = [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,1,1,1,-1,-1,-1,-1],[-1,-1,-1,-1,1,1,1,-1,-1,-1,-1],[-1,-1,1,1,1,1,1,1,1,-1,-1],
[-1,-1,1,1,1,1,0,0,1,-1,-1],[-1,-1,1,1,1,1,1,1,1,-1,-1],[-1,-1,-1,-1,1,1,1,-1,-1,-1,-1],
[-1,-1,-1,-1,1,1,1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]

def generate_moves(board):
    moves = []
    for i in range(2,9):
        for j in range(2,9):
            if board[i][j] == 1:
                if board[i+1][j] == 1 and board[i+2][j] == 0:
                    moves.append(board.right())
                if board[i-1][j] == 1 and board[i-2][j] == 0:
                    moves.append(board.left())
                if board[i][j+1] == 1 and board[i][j+2] == 0:
                    moves.append(board.down())
                if board[i][j-1] == 1 and board[i][j-2] == 0:
                    moves.append(up)

def bfs(board):
    if counter == 30 and board[5][5]==1:
        return backtrack(board)
