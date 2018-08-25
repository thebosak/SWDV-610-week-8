'''
Brad Bosak
SWDV-610 Data Structures Final Project
8/22/2018

This is the knight's tour program adapted by
Brad Miller on 2005-02-24.
Copyright (c) 2005 Brad Miller, David Ranum, Luther College. All rights reserved.

This program successfully completes one tour around a chess board of a given size
using a depth first search algorithm and a graph data structure
'''

from classes import Graph

def createKnightGraph(boardSize):             #this function creates the graph that
    knightGraph = Graph()                     #will be used in the tour.  "boardSize" is the length of 
    for row in range(boardSize):              #a row or column of the chess board
        for col in range(boardSize):
            nodeId = assignNodeId(row,col,boardSize)         #calls helper function to create nodes in the graph
            newPositions = genLegalMoves(row,col,boardSize)  #calls helper function to generate legal moves from a node
            for e in newPositions:
                nid = assignNodeId(e[0],e[1],boardSize)
                knightGraph.addEdge(nodeId,nid)              #adds edge between initial node and all legal knight's moves
    return knightGraph

def assignNodeId(row, column, size):                         #helper function to assign nodes
    return (row * size) + column

def genLegalMoves(x,y,boardSize):
    newMoves = []
    moveOffsets = [(-1,-2),(-1,2),(-2,-1),(-2,1),            #the knight's moves make it one of my favorite
                   ( 1,-2),( 1,2),( 2,-1),( 2,1)]            #pieces in chess!
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX,boardSize) and \
                        legalCoord(newY,boardSize):          #calls helper function to only add legal moves
            newMoves.append((newX,newY))
    return newMoves

def legalCoord(x,boardSize):                  #helper function determine if available moves are on the board or off
    if x >= 0 and x < boardSize:
        return True
    else:
        return False

#Knight's tour depth first search where n is current depth of tree
#path is a list of nodes visited up to this point
#u is the current node we are exploring
#limit is the number of nodes in the path
def knightTour(n,path,u,limit):
        u.setColor('gray')                                   #set initial node color gray to mark as visited
        path.append(u)                                       #append the current node to the path list
        if n < limit:
            nbrList = list(u.orderByAvail(u))                #calls helper function which will have next node visited
            i = 0                                            #be the one with the least amount of future moves
            done = False
            while i < len(nbrList) and not done:
                if nbrList[i].getColor() == 'white':         #set to white to mark as not visited
                    done = knightTour(n+1, path, nbrList[i], limit)    #recursive call to knightTour to continue through the nodes
                i = i + 1
            if not done:                                     #backtrack if we hit a dead end
                path.pop()
                u.setColor('white')
        else:
            done = True
        return path                                          #changed function to return path to see all nodes visited in what order

'''main function to call the knightTour function on the first vertex of a chess board with 25 spaces
The current depth is 0, we haven't visited any nodes yet, and the limit of our search is 25'''
def main():
    final_path = knightTour(0,[],createKnightGraph(5).getVertex(0), 25)
    for vertex in final_path:                     #for each vertex in the visited path,
        print(vertex.getId())                     #print the vertex ID
        
main()