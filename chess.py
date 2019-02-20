def printBoard(board):
    for i in range(63,-1,-1):
        if(board[i]==0):
            if(board[i]%2==0):

def main():
    board = [13,11,12,14,15,12,11,13,10,10,10,10,10,10,10,10]
    for i in range(16,48,1):
        board += [0]
    board += [20,20,20,20,20,20,20,20,23,21,22,24,25,22,21,23]
    printBoard(board)
    
main()
