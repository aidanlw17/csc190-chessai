def PrintBoard(board):
    boardstr = ""
    linestr = ""
    cnt = 1
    for i in range(63,-1,-1):
        if(board[i]==0):
            if(cnt%2!=0):
                if(i%2==0):
                    linestr += "__ "
                else:
                    linestr += "## "
            else:
                if(i%2==0):
                    linestr += "## "
                else:
                    linestr += "__ "
        else:
            linestr += (str(board[i]) + " ")
        if(i%8==0):
            linestr += " \n"
            boardstr += linestr
            linestr = ""
            cnt += 1
    print(boardstr)
    print("_ black, # white, 20 offset black, 10 offset white")
    return 0

def GenBoard():
    board = [13,11,12,15,14,12,11,13,10,10,10,10,10,10,10,10]
    for i in range(16,48,1):
        board += [0]
    board += [20,20,20,20,20,20,20,20,23,21,22,25,24,22,21,23]
    return board

def GetPlayerPositions(board, player):
    positions = []
    for i in range(0,64,1):
        if((board[i]-player)>=0 and (board[i]-player)<=5):
            positions += [i]
    return positions
        
def GetPieceLegalMoves(board,position):
    piece = board[position]

def main():
    #print and generate the board
    board = GenBoard()
    PrintBoard(board)

    #PLAYER positions
    print("white positions: \n")
    print(GetPlayerPositions(board,10))
    print("black positions: \n")
    print(GetPlayerPositions(board,20))

main()




