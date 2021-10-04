# TAROT GAME
# MATHEUS BALÃO
# DIVINATION DARK MAGIC

import tarot_cards
from random import shuffle
from random import randint
from time import sleep
import textwrap


class Tarot:
    deck = []
    drawed = []
    name = ''
    line_size = 90

    def draw_line(self):
        print("*" * self.line_size)

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

    def start_taro(self):
        self.draw_line()
        print("TARO DIVINATION DARK MAGICK".center(self.line_size))
        self.draw_line()

    def shuffle_deck_three_times(self):
        answer = input(f"Are you ready to start and to shuffle your deck 3 times, {self.name}? (Yes-No)\n")
        if answer != 'Yes' or answer == 'yes':
            answer = input(f"Are you ready to start and to shuffle your deck 3 times, {self.name}? (Yes-No)\n")
        else:
            for i in range(3):
                print(f"Deck shuffle: {i + 1}")
                shuffle(self.deck)
                sleep(1)

    def draw_fifteen(self):
        for i in range(15):
            self.drawed.append(self.deck.pop((len(self.deck) - 1) - i))
        for j in range(15):
            self.draw_line()
            print((str(j + 1) + ": " + self.drawed[j]["name"]).center(self.line_size))
            self.draw_line()
            print("\n".join(textwrap.wrap(self.drawed[j]["meaning"], self.line_size)))

    def invocation(self):
        self.draw_line()
        print("SACRED INVOCATION".center(self.line_size))
        self.draw_line()
        print("\n".join(textwrap.wrap(tarot_cards.initial_invocation, self.line_size)))
        self.draw_line()

    def get_name(self):
        self.name = input("What is your name, Master?\n")
        sleep(1)
        print(f"Welcome, Master {self.name}.")
        self.draw_line()
        sleep(1)
        print(f"Take your time to make the following invocation with meaning and purpouse.")
        sleep(1)
        tarot.invocation()


tarot = Tarot()
tarot.fillDeck()
tarot.start_taro()
tarot.get_name()
sleep(1)
tarot.shuffle_deck_three_times()
tarot.draw_fifteen()
