from chess import *

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
moves = GetPieceLegalMoves(board,63)
print(moves)
moves = GetPieceLegalMoves(board,62)
print(moves)
moves = GetPieceLegalMoves(board,59)
print(moves)
moves = GetPieceLegalMoves(board,57)
print(moves)
moves = GetPieceLegalMoves(board,60)
print(moves)
moves = GetPieceLegalMoves(board,49)
print(moves)
moves = GetPieceLegalMoves(board,49)
moves = GetPieceLegalMoves(board,49)
moves = GetPieceLegalMoves(board,49)
moves = GetPieceLegalMoves(board,49)
moves = GetPieceLegalMoves(board,49)
moves = GetPieceLegalMoves(board,49)
moves = GetPieceLegalMoves(board,49)
print(moves)
isThreat=IsPositionUnderThreat(board,62,20)
print(isThreat)