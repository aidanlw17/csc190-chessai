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
    #find which team the piece at the position belongs to
    #determine which board positions are under threat by other team
    #positions not under threat and available for the type of piece are legal moves
    piece = board[position]
    pieces = {
        10: WPawnLM,
        11: WKnightLM,
        # 12: WBishopLM,
        # 13: WRookLM,
        # 14: WQueenLM,
        # 15: WKingLM,
        20: BPawnLM,
        21: BKnightLM,
        # 22: BBishopLM,
        # 23: BRookLM,
        # 24: BQueenLM,
        # 25: BKingLM
    }
    return pieces[piece](board,position)

def WPawnLM(board, position):
    moves=[]
    #starting two square jump
    if(position<=15 and board[position+16]==0):
        moves+= [position+16]

    #next square
    if(position<56 and board[position+8]==0):
        moves += [position +8]
    
    #diagonal squares
    if(position<56 and position%8!=0 and position%7!=0):
        if(board[position+7]>=20):
            moves+=[position+7]
        if(board[position+9]>=20):
            moves+=[position+9]
    elif(position<56 and position%8==0):
        if(board[position+9]>=20):
            moves+=[position+9]
    elif(position<56 and position%7==0):
        if(board[position+7]>=20):
            moves+=[position+7]
    return moves

def BPawnLM(board,position):
    moves=[]
    #starting two square jump
    if(position>=48 and board[position-16]==0):
        moves+= [position-16]

    #next square
    if(position>7 and board[position-8]==0):
        moves += [position-8]    

    #diagonal squares
    if(position>7 and position%8!=0 and position%7!=0):
        if(board[position-7]<16 and board[position-7]>0):
            moves+=[position-7]
        if(board[position-9]<16 and board[position-9]>0):
            moves+=[position-9]
    elif(position>7 and position%8==0):
        if(board[position-7]<16 and board[position-7]>0):
            moves+=[position-7]
    elif(position>7 and position%7==0):
        if(board[position-9]<16 and board[position-9]>0):
            moves+=[position-9]
    return moves

def WKnightLM(board,position):
    moves=[]
    a = [-10,-17,6,15,17,10,-6,-15]
    if(position%8==0):
        for p in a[4:]:
            if((position+p)>=0 and (position+p)<64):
                if(position)
    elif(position%7==0):




def main():
    #print and generate the board
    board = GenBoard()
    PrintBoard(board)
    
    #PLAYER positions
    print("white positions: \n")
    print(GetPlayerPositions(board,10))
    print("black positions: \n")
    print(GetPlayerPositions(board,20))

    #get piece legal moves
    moves = GetPieceLegalMoves(board,49)
    print(moves)

main()




