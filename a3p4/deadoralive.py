# JTSK-350112
# a3 4.py
# Wossen Hailemariam
# w.hailemariam@jacobs-university.de



from cards import Deck, Card
from blackjack import Player, Dealer, Blackjack

#the game
class Deadoralive(object):
    
    print("DEADORALIVE")

    def __init__(self):
        self._deck = Deck()
        self._deck.shuffle()
        self._player = Player([self._deck.deal(), self._deck.deal()])
        self._dealer = Dealer([self._deck.deal(), self._deck.deal()])

   
    def getValue(self):
        """Returns the number of points in the hand."""
        count = 0
        for card in self._cards:
            if card.rank > 9:
                count += 10
            elif card.rank == 1:
                count += 11
            else:
                count += card.rank
            return count



    def compare(self,other):
       """compare the cards and returns message"""


       """we can compare by using the value function"""
       playerpoint = self._player.getValue()
       dealerpoint = other._dealer.getValue()

       if playerpoint > dealerpoint:
           print("\nPlayer Won")
       elif playerpoint < dealerpoint:
           print("\nDealer Won")


    def playdead(self):
        print("Player:\n", self._player)
        print("Dealer:\n", self._dealer)
        while True:
            if len(self._deck._cards) == 0:
                print("game has ended")
                break
            else:
                _deadoralive.compare(self._player,self._dealer)


def main():
    game = Deadoralive()
    game.playdead()
    

main()
  



    