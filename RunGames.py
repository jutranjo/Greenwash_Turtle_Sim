from TurtleSim import *

twoPlayerDeck = {
    #GreenwashValue:Quantity of cards
    0:2,
    1:2,
    2:4,
    3:6,
    4:4,
    5:2
}

#Count for the game
startingHandSize = 5
turnsToTake = 5

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

#Plays out a number of turns specified in turnsToTake
for _ in range(turnsToTake):
    cardDrawn = DrawRandomCard(DeckList)
    PlayerHand.Draw(cardDrawn)
    CurrentGame.PlaySafe()

#Prints result of game
print(CurrentGame.GreenWash,CurrentGame.Industry)