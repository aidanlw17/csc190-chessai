from chess import *

#print and generate the board
board = GenBoard()

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
                    possible=True
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
            possible=False
            for i in candMoves:
                if(move==i):
                    possible=True
                    break
            if(possible):
                tmp=board[piece]
                board[piece]=0
                board[move]=tmp
        else:
            print("You do not have a piece in that position! \n")

