from chess import *
import time

def getTime():
    h=True
    while(h):
        if(time.process_time()>10):
        h=False
    print(time.process_time())

def chessPlayer(board,player):