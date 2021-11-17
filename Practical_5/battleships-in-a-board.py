#board =list(input())
board = [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]
def check(board):
    if len(board) == 0: 
        return 0
    result = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (board[i][j] == '.'): 
                continue
            if i > 0 and board[i - 1][j] == 'X': 
                continue
            if j > 0 and board[i][j - 1] == 'X':
                continue
            result += 1         
    return result

print(check(board))
