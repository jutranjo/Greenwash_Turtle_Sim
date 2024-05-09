from TurtleSim import *
import matplotlib.pyplot as plt

twoPlayerDeck = {
    #GreenwashValue:Quantity of cards
    0:2,
    1:2,
    2:4,
    3:6,
    4:4,
    5:2
}

#Rules for the game
startingHandSize = 5
turnsToTake = 5

#Simulation run size
simRunSize = 10000

IndustryCounts = {}

for _ in range(simRunSize):
    #Prepare Deck
    DeckList = TurnDeckIntoListOfCards(twoPlayerDeck)

    #Initialize game state
    CurrentGame = GameState()
    PlayerHand = CurrentGame.Hand

    #Prepare Starting Hand
    for _ in range(startingHandSize):
        PlayerHand.Draw(DrawRandomCard(DeckList))

    #Play the 2 highest greenwash cards:
    CurrentGame.playHighestGreenWash()
    CurrentGame.playHighestGreenWash()
    #Play 1 card
    CurrentGame.PlaySafe()

    #Plays out a number of turns specified in turnsToTake
    for _ in range(turnsToTake):
        cardDrawn = DrawRandomCard(DeckList)
        PlayerHand.Draw(cardDrawn)
        CurrentGame.PlaySafe()

    endGameScore = CurrentGame.Industry

    if endGameScore in IndustryCounts:
        IndustryCounts[endGameScore] += 1
    else:
        IndustryCounts[endGameScore] = 1

IndustryScores = list(IndustryCounts.keys())
IndustryGames = list(IndustryCounts.values())

plt.bar(IndustryScores, IndustryGames)

plt.title("Results after playing "+str(simRunSize)+" games")
plt.xlabel("End of game Industry value")
plt.ylabel("Number of games with that score")

plt.show()