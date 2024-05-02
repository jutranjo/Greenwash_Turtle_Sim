import copy

class GameState:
    def __init__(self):
        self.Hand = Hand()
        self.Industry = 0
        self.GreenWash = 0

    def PlaySafe(self):
        if (self.GreenWash>self.Industry):
            IndustrySpace = self.GreenWash-self.Industry
            self.playSomeIndustry(IndustrySpace)
        else:
            self.playHighestGreenWash()

    def playHighestGreenWash(self):
        CardsToCheck = self.Hand.HeldCards
        HighestGreenWash = max(CardsToCheck, key=lambda card: card.GreenWashValue)
        CardsToCheck.remove(HighestGreenWash)
        self.GreenWash = self.GreenWash + HighestGreenWash.GreenWashValue

    def playSomeIndustry(self,IndustrySpace):
        originalHand = self.Hand.HeldCards
        CardsToCheck = copy.deepcopy(originalHand)
        while CardsToCheck:
            HighestIndustry = min(CardsToCheck, key = lambda card: IndustrySpace - card.IndustryValue)
            CardsToCheck.remove(HighestIndustry)
            if (IndustrySpace - HighestIndustry.IndustryValue >= 0):
                CardToRemove = min(originalHand, key = lambda card: HighestIndustry.IndustryValue - card.IndustryValue)
                self.Hand.HeldCards.remove(CardToRemove)
                self.Industry = self.Industry + HighestIndustry.IndustryValue
                break
        else:
            self.playHighestGreenWash()
        
        

class Hand:
    def __init__(self):
        self.HeldCards = []
    def Draw(self, card):
        self.HeldCards.append(card)

class Card:
    def __init__(self,GreenWashValue):
        self.GreenWashValue = GreenWashValue
        self.IndustryValue = 6 - GreenWashValue