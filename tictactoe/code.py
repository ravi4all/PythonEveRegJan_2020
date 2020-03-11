import random
import time

combinations = [
    [1,2,3],[4,5,6],[7,8,9],
    [1,4,7],[2,5,8],[3,6,9],
    [1,5,9],[3,5,7]
]

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

def userMove(ch):
    pos = int(input("Enter your pos : "))
    positions[pos - 1] = ch
    gameBoard()
    posOccupied.append(pos)
    msg = checkWinner(pos,ch)
    return msg

def cpuMove(ch):
    cpu_pos = random.randint(0,8)
    print("CPU Picked",cpu_pos)
    if cpu_pos in posOccupied:
        cpuMove(ch)
    else:
        positions[cpu_pos - 1] = ch
        gameBoard()
        posOccupied.append(cpu_pos)
        msg = checkWinner(cpu_pos,ch)
        return msg

def checkWinner(pos,ch):
    for i in range(len(combinations)):
        if pos in combinations[i]:
            index = combinations[i].index(pos)
            combinations[i][index] = ch

    for i in range(len(combinations)):
        if combinations[i][0] == ch and combinations[i][1] == ch and combinations[i][2] == ch:
            return "win"

    # print(combinations)

def main():
    gameBoard()
    ch = input("Enter your choice : X | O : ")
    if ch == "X":
        cpu_ch = 'O'
    else:cpu_ch = 'X'
    while True:
        print(positions)
        msg = userMove(ch)
        if msg == "win":
            print("User win")
            break
        time.sleep(2)
        msg = cpuMove(cpu_ch)
        if msg == "win":
            print("CPU Win")
            break

main()