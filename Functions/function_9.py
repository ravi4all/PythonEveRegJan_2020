def playerHealth():
    health = 50
    return health

def enemyHealth():
    health = 40
    return health

def timer():
    timeLeft = 0
    return timeLeft

def game():
    h1 = playerHealth()
    h2 = enemyHealth()
    time = timer()
    if time == 0:
        if h1 > h2:
            print("Player is winning")
        else:
            print("Enemy is winning")

game()