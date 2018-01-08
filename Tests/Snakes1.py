import random

# Snakes and Ladders dictionary
SaLdic = {6: 17,
          14: 3,
          20: 15,
          24: 26,
          30: 44,
          39: 33,
          49: 62,
          66: 53,
          69: 58,
          79: 67,
          82: 86,
          84: 71,
          88: 36,
          }


# Player class
class Player:
    def __init__(self, inPlayerNum):
        self.playerPos = 1
        self.playerNum = inPlayerNum

    def updatePosition(self, inPos):
        self.playerPos = inPos

    def getPosition(self):
        return self.playerPos

    def getPlayerNum(self):
        return self.playerNum


# Function to handle the players turn
def gameMaster(inPlayer):
    global winner
    # check for game winner
    if inPlayer.getPosition() == 90:
        print("Player %i is the Winner!" % inPlayer.getPlayerNum())
        winner = True

    # run dice rolls and movements
    if winner == False:
        print("\n----Player %i Hit enter to roll----" % inPlayer.getPlayerNum())
        # Uncomment to require space to be pressed before jumping turns
        # input()
        roll = rollDice()
        print("You rolled: %i" % roll)
        movePlayer(inPlayer, roll)
        checkPosition(inPlayer)


# Function to return the Integer value of a 6 side dice roll
def rollDice():
    return random.randint(1, 6)


# Handle player movements
def movePlayer(inPlayer, roll):
    if inPlayer.getPosition() + roll <= 90:
        inPlayer.updatePosition(inPlayer.getPosition() + roll)
        print("You are at spot %i" % inPlayer.getPosition())
    else:
        print("You rolled too far")


# Checks player landing position and adjusts if snake or ladder
def checkPosition(inPlayer):
    for pos in SaLdic:
        if pos == inPlayer.getPosition():
            if pos < SaLdic[pos]:
                print("You climbed a Ladder to spot %i" % SaLdic[pos])
            else:
                print("You rode a Snake to spot %i" % SaLdic[pos])
            inPlayer.updatePosition(SaLdic[pos])


# Program entrance
if __name__ == '__main__':
    global winner
    winner = False
    numPlayers = int(input('Enter number of players: '))
    playerList = []

    for i in range(0, numPlayers):
        playerList.append(Player(i + 1))

    while winner == False:
        for i in playerList:
            if winner == False:
                gameMaster(i)