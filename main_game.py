# TAROT GAME
# MATHEUS BALÃO
# DIVINATION DARK MAGIC

import tarot_cards
from random import shuffle
from time import sleep
from textwrap import wrap
from datetime import date


class Tarot:
    deck = []
    drawed = []
    name = ''
    line_size = 60
    card_size = 60
    shuffle = False
    current_date = date.today()
    dominant_cards = []
    pontential_cards_upper_left = []
    pontential_cards__upper_right = []
    assist_cards = []
    destiny_cards = []
    purpouse = ""

    def draw_line(self):
        print("*" * self.line_size)

    def draw_card_line(self):
        print("_" * self.card_size + "\n")

    def draw_card(self):
        print("*" * self.card_size)

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
        tarot.fillDeck()
        tarot.get_name()
        tarot.get_purpouse()
        tarot.shuffle_deck_three_times()
        tarot.draw_fifteen()
        tarot.show_instructions()
        tarot.show_dominant_cards()
        sleep(5)
        tarot.show_potential_cards_upper_right()
        sleep(5)
        tarot.show_pontetial_cards_upper_left()
        sleep(5)
        tarot.show_assist_cards()
        sleep(5)
        tarot.show_destiny_cards()

    def invocation(self):
        self.draw_line()
        print("SACRED INVOCATION".center(self.line_size))
        self.draw_line()
        print("\n".join(wrap(tarot_cards.initial_invocation, self.line_size)) + "\n")
        self.draw_line()

    def get_name(self):
        self.name = input("What is your name, Master?\n-> ")
        sleep(1)
        print(f"Welcome, Master {self.name}.")
        sleep(1)
        print(f"Today's date is {self.current_date}.")
        sleep(1)
        print(f"Take your time to do the following invocation with meaning and purpouse.\n")
        sleep(2.5)
        self.invocation()
        sleep(2)

    def get_purpouse(self):
        self.purpouse = input(
            "What is the purpose of your search, Master?\n-> ")
        sleep(1)

    def shuffle_deck_three_times(self):
        while self.shuffle == False:
            answer = input(
                f"Master {self.name}, would you like to start shuffling your cards?\n-> ")
            if answer == "Yes":
                for i in range(3):
                    print(f"Deck shuffle: {i + 1}")
                    shuffle(self.deck)
                    sleep(1)
                    self.shuffle = True

    def draw_fifteen(self):
        for i in range(15):
            self.drawed.append(self.deck.pop((len(self.deck) - 1) - i))
        for j in range(15):
            if j == 0 or j == 1 or j == 2:
                self.dominant_cards.append(self.drawed[j])
            if j == 12 or j == 8 or j == 4:
                self.pontential_cards_upper_left.append(self.drawed[j])
            if j == 3 or j == 7 or j == 11:
                self.pontential_cards__upper_right.append(self.drawed[j])
            if j == 13 or j == 9 or j == 5:
                self.assist_cards.append(self.drawed[j])
            if j == 6 or j == 10 or j == 13:
                self.destiny_cards.append(self.drawed[j])


    def show_instructions(self):
        self.draw_line()
        print("INSTRUCTIONS".ljust(self.line_size) + '\n')
        self.draw_line()
        sleep(1)
        print("About the Court Cards".ljust(self.line_size) + '\n')
        print("\n".join(
            wrap(tarot_cards.information_guide["court_cards"], self.line_size)) + "\n")
        self.draw_line()
        sleep(1)
        print("About group cards".ljust(self.line_size) + '\n')
        print("\n".join(
            wrap(tarot_cards.information_guide["groups"], self.line_size)) + "\n")
        self.draw_line()
        print("About neighbord cards".ljust(self.line_size) + '\n')
        print("\n".join(
            wrap(tarot_cards.information_guide["neighbord_cards"], self.line_size)) + "\n")

    def show_dominant_cards(self):
        self.draw_line()
        print("DOMINANT CARDS".ljust(self.line_size) + '\n')
        print("\n".join(
            wrap(tarot_cards.information_guide["assist_cards"], self.line_size)) + "\n")
        for i, card in enumerate(self.dominant_cards):
            self.draw_card()
            print(
                "+" + f"Card nº {i + 1}: {card['name']}".center(self.card_size - 2) + "+")
            self.draw_card_line()
            print("\n".join(wrap(card["meaning"], self.card_size)) + "\n")
            self.draw_card_line()

    def show_potential_cards_upper_right(self):
        number = 0
        self.draw_line()
        print("PONTENTIAL CARDS UPPER RIGHT".ljust(self.line_size) + '\n')
        print("\n".join(
            wrap(tarot_cards.information_guide["potential_right"], self.line_size)) + "\n")
        for card in self.pontential_cards__upper_right:
            number += 4
            self.draw_card()
            print(
                "+" + f"Card nº {number}: {card['name']}".center(self.card_size - 2) + "+")
            self.draw_card_line()
            print("\n".join(wrap(card["meaning"], self.card_size)) + "\n")

    def show_pontetial_cards_upper_left(self):
        number = 1
        self.draw_line()
        print("PONTENTIAL CARDS UPPER LEFT".ljust(self.line_size) + '\n')
        print("\n".join(
            wrap(tarot_cards.information_guide["potential_left"], self.line_size)) + "\n")
        for card in self.pontential_cards_upper_left:
            number += 4
            self.draw_card()
            print(
                "+" + f"Card nº {number}: {card['name']}".center(self.card_size - 2) + "+")
            self.draw_card_line()
            print("\n".join(wrap(card["meaning"], self.card_size)) + "\n")
            self.draw_card_line()

    def show_assist_cards(self):
        number = 2
        self.draw_line()
        print("ASSISTANT CARDS".ljust(self.line_size) + '\n')
        print("\n".join(
            wrap(tarot_cards.information_guide["assist_cards"], self.line_size)) + "\n")
        for card in self.assist_cards:
            number += 4
            self.draw_card()
            print(
                "+" + f"Card nº {number}: {card['name']}".center(self.card_size - 2) + "+")
            self.draw_card_line()
            print("\n".join(wrap(card["meaning"], self.card_size)) + "\n")

    def show_destiny_cards(self):
        number = 3
        self.draw_line()
        print("DESTINY CARDS".ljust(self.line_size) + '\n')
        print("\n".join(
            wrap(tarot_cards.information_guide["destiny_cards"], self.line_size)) + "\n")
        for card in self.destiny_cards:
            number += 4
            self.draw_card()
            print(
                "+" + f"Card nº {number}: {card['name']}".center(self.card_size - 2) + "+")
            self.draw_card_line()
            print("\n".join(wrap(card["meaning"], self.card_size)) + "\n")

    def save(self):
        pass


tarot = Tarot()
tarot.start_taro()

tarot.save()
