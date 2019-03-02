from chess import *

#print and generate the board
board = GenBoard()
wKingPosition=4
bKingPosition=60
done=False
while not(done):
    possible=False
    while not(possible):
        print("Board:\n")
        PrintBoard(board)
        print("--------White's Move--------\n")
        piece=int(input("Which position would you like to move?\n"))
        if(board[piece]<=15):
            move=int(input("Where would you like to move the piece?\n"))
            candMoves=GetPieceLegalMoves(board,piece)
            for i in candMoves:
                if(move==i):
                    [kingissafe,threats]=KingSafe(10,board)
                    if kingissafe:
                        possible=True
                        break
                    else:
                        for k in threats:
                            if(move==k):
                                tmpb = board
                                tmpb[move]=board[piece]
                                tmpb[piece]=0
                                if (KingSafe(10,tmpb))[1]== -1:
                                    possible=True
                                    break
                                else:
                                    print("This move does not fully remove your king from check! Try again.")
                                    break
            if(possible):
                tmp=board[piece]
                board[piece]=0
                board[move]=tmp

        else:
            print("You do not have a piece in that position! \n")

    possible=False
    print(board)
    while not(possible):
        print("Board:\n")
        PrintBoard(board)
        print("--------Black's Move--------\n")
        piece=int(input("Which position would you like to move?\n"))
        if(board[piece]>=20):
            move=int(input("Where would you like to move the piece?\n"))
            candMoves=GetPieceLegalMoves(board,piece)
            print(candMoves)
            possible=False
            for i in candMoves:
                if(move==i):
                    [kingissafe,threats]=KingSafe(20,board)
                    if kingissafe:
                        possible=True
                        break
                    else:
                        for k in threats:
                            if(move==k):
                                tmpb=board
                                tmpb[move]=board[piece]
                                tmpb[piece]=0
                                if (KingSafe(20,tmpb))[1]==-1:
                                    possible=True
                                    break
                                else:
                                    print("This move does not fully remove your king from check! Try again.")
                                    break
            if(possible):
                tmp=board[piece]
                board[piece]=0
                board[move]=tmp
            else:
                print("That move is not possible.")
        else:
            print("You do not have a piece in that position! \n")

