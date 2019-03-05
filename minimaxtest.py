from mima import *
from chess import *
from gametree import *

board=GenBoard()
PrintBoard(board)
#White move
board[17]=board[9]
board[9]=0
#Generate gametree for current position
gametree=GameTree(board,0,17,9,3)
#Populate gametree to required depth
gametree.populateTree(board,20)
#Init minimax for gametree
mm=MiniMax(gametree)
#Search for and return best move
best=mm.minimaxSearch(gametree,20)
PrintBoard(board)
print(board)
print(gametree.getCandMoves())
# print("best is:")
# print(best)
# print("Best move is:")
# print(best.value[0])
# print("Inital piece move to this board:")
# print(best.moveToThisBoard[0])
# print("Piece moved to:")
# print(best.moveToThisBoard[1])