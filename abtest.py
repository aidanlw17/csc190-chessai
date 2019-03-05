from ab import *
from gametree import *
from chess import *

board=GenBoard()
gametree=GameTree(board,0)
gametree.populateTree(board,3,20)
ab=AlphaBeta(gametree)
best = ab.alpha_beta_search(gametree)
print(best)