# TAROT GAME
# MATHEUS BALÃO
# DIVINATION DARK MAGIC

import tarot_cards
from random import shuffle
from random import randint


class Tarot:
    deck = []
    drawed = []

    def draw_line(self):
        print("*" * 40)
    def fillDeck(self):
        for i in range(14):
            # Adding Wards
            self.deck.append(tarot_cards.wards_tarot_cards[i])
        for i in range(14):
            # Adding Cups
            self.deck.append(tarot_cards.cups_tarot_cards[i])
        for i in range(14):
            # Adding Swords
            self.deck.append(tarot_cards.swords_tarot_cards[i])
        for i in range(14):
            # Adding Disks
            self.deck.append(tarot_cards.disks_tarot_cards[i])
        for i in range(22):
            # Adding Majors
            self.deck.append(tarot_cards.major_tarot_cards[i])

    def shuffle_deck_three_times(self):
        for i in range(3):
            shuffle(self.deck)

    def draw_fifteen(self):
        for i in range(15):
            self.drawed.append(self.deck.pop((len(self.deck) - 1) - i))
        for j in range(15):
            self.draw_line()
            print(self.drawed[j]["name"])


tarot = Tarot()
tarot.fillDeck()
tarot.shuffle_deck_three_times()
tarot.draw_fifteen()
