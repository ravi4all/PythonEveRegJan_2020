positions = [1,2,3,4,5,6,7,8,9]
posOccupied = []
def gameBoard():
    print("""
        {} | {} | {} 
       ------------
        {} | {} | {}
       ------------
        {} | {} | {}
    """.format(positions[0],positions[1],positions[2],
               positions[3], positions[4], positions[5],
               positions[6], positions[7], positions[8]))

def userMove():
    pass

def cpuMove():
    pass

def checkWinner():
    pass

def main():
    gameBoard()

main()