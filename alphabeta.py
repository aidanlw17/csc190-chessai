from gametree import *
from chess import *

class AlphaBeta:
    def __init__(self,gametree):
        self.gametree=gametree
        self.children=gametree.getChildren()

    def abSearch(self,node,player):
        inf=float('inf')
        bestVal=-inf
        beta=inf
        children=self.getChildren(node)
        bestState=None
        for i in children:
            val=self.minTurn(i,bestVal,beta)
            if val>bestVal:
                bestVal=val
                bestChild=i
        #Child node as a whole
        return bestChild

    def maxTurn(self,node,alpha,beta):
        if(self.atBottom(node)):
            return self.getNodeValue(node)
        inf=float('inf')
        val=-inf
        children=self.getChildren(node)
        for i in children:
            val=max(val,self.minTurn(i,alpha,beta))
            if(val>=beta):
                return val
            alpha=max(alpha,val)
        return val

    def minTurn(self,node,alpha,beta):
        if(self.atBottom(node)):
            return self.getNodeValue(node)
        inf=float('inf')
        val=inf
        children=self.getChildren(node)
        for i in children:
            val=min(val,self.minTurn(i,alpha,beta))
            if(val<=alpha):
                return val
            beta=min(beta,val)
        return val

    def getChildren(self,node):
        if(node!=None):
            return node.getChildren()
    
    def atBottom(self,node):
        if(len(node.getChildren())==0):
            return True
        return False

    def getNodeValue(self,node):
        return node.value[0]
