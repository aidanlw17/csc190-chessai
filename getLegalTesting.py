from chess import *
board = GenBoard()
PrintBoard(board)
print("Next")
board[27]=board[4]
board[4]=0
PrintBoard(board)
print("legal moves for queen @ 27:")
legal=GetPieceLegalMoves(board,27)
print(legal)
print("")
board[32]=board[27]
board[27]=0
PrintBoard(board)
board[42]=board[50]
board[50]=0
PrintBoard(board)
board[19]=board[11]
board[11]=0
[isThreat,threats]=IsPositionUnderThreat(board,59,20)
print(isThreat)
print("The threats are:")
print(threats)
print("###########")
legal=GetPieceLegalMoves(board,32)
print("Legal moves for queen are:")
print(legal)
print(board)
PrintBoard(board)
blackCheck=isInCheck(board,20)
print("Black is checked?")
print(blackCheck)
#Getting to checkmate
board[16]=board[8]
board[8]=0
board[40]=board[48]
board[48]=0
board[49]=0
board[41]=board[32]
board[32]=0
PrintBoard(board)
blackCheckMate=isCheckmate(board,20)
print("Black is checkmated?")
print(blackCheckMate)