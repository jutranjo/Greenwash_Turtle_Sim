from TurtleSim import *


def test_OpeningHandPlay():
    TestGame = GameState()
    PlayerHand = TestGame.Hand

    PlayerHand.Draw(Card(0))
    PlayerHand.Draw(Card(2))
    PlayerHand.Draw(Card(3))
    PlayerHand.Draw(Card(3))
    PlayerHand.Draw(Card(4))

    TestGame.playHighestGreenWash()
    assert TestGame.GreenWash == 4

    TestGame.playHighestGreenWash()
    assert TestGame.GreenWash == 7

    TestGame.PlaySafe()
    assert TestGame.Industry == 6
    #Opening Hand Set

    PlayerHand.Draw(Card(3))
    TestGame.PlaySafe()
    assert TestGame.GreenWash == 10

    PlayerHand.Draw(Card(1))
    TestGame.PlaySafe()
    assert TestGame.Industry == 10