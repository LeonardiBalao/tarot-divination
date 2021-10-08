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
    answer = ''
    shuffle = False
    anotherFactor = False
    factor = ''
    current_date = date.today()
    dominant_cards = []
    potential_cards_upper_left = []
    potential_cards__upper_right = []
    assist_cards = []
    destiny_cards = []
    save = ''

    def draw_line(self):
        print("*" * self.line_size)

    def draw_card_line(self):
        print("_" * self.card_size + "\n")

    def draw_card(self):
        print("*" * self.card_size)

    def get_last_name(self):
        last_name = self.name.split()
        return last_name[len(last_name) - 1]

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

    def invocation(self):
        self.draw_line()
        print("\033[1m" + "SACRED INVOCATION".center(self.line_size) + "\033[0m")
        self.draw_line()
        print("\n".join(wrap(tarot_cards.initial_invocation, self.line_size)) + "\n")
        self.draw_line()

    def closing_invocation(self):
        self.draw_line()
        print("\033[1m" + "CLOSING INVOCATION".center(self.line_size) + "\033[0m")
        self.draw_line()
        print("\n".join(wrap(tarot_cards.closing_invocation, self.line_size)))
        self.draw_line()

    def get_name(self):
        sleep(1)
        self.name = input("Start by telling me your full name, Master.\n-> ")
        sleep(1)
        self.draw_line()
        print(f"Welcome, Master {self.get_last_name()}.".center(self.line_size))
        sleep(1)
        print(f"Today's date is: {self.current_date}.".center(self.line_size))
        sleep(1)
        self.draw_line()
        print("\n".join(wrap(
            "Take your time to do the following invocation with meaning and purpouse.", self.line_size)))
        sleep(1.5)
        self.invocation()
        while self.answer != "Yes":
            self.answer = input("\n".join(wrap("Did you really meant it?", self.line_size)) + "(Yes or No)\n")
        sleep(1.5)

    def get_factor(self):
            self.draw_line()
            self.answer = input("\n".join(wrap(
                'Tell me, what is the main factor governing your situation?', self.line_size)) + "\n-> ")
            self.factor = self.answer

    def shuffle_deck(self):
        while self.shuffle == False:
            answer = input(
                f"Master {self.name}, would you like to start shuffling your cards?\n-> ")
            if answer == "Yes":
                for i in range(666):
                    print(f"Deck shuffle: {i + 1}")
                    shuffle(self.deck)
                self.shuffle = True

    def draw_fifteen(self):
        for i in range(15):
            self.drawed.append(self.deck.pop((len(self.deck) - 1) - i))
        for j in range(15):
            if j == 0 or j == 1 or j == 2:
                self.dominant_cards.append(self.drawed[j])
            if j == 12 or j == 8 or j == 4:
                self.potential_cards_upper_left.append(self.drawed[j])
            if j == 3 or j == 7 or j == 11:
                self.potential_cards__upper_right.append(self.drawed[j])
            if j == 13 or j == 9 or j == 5:
                self.assist_cards.append(self.drawed[j])
            if j == 6 or j == 10 or j == 14:
                self.destiny_cards.append(self.drawed[j])

    def show_instructions(self):
        self.draw_line()
        print("\033[1m" + "INSTRUCTIONS".center(self.line_size) + "\033[0m")
        self.draw_line()
        sleep(1)
        print(
            "\033[1m" + "About the Court Cards".ljust(self.line_size) + "\033[0m" + '\n')
        print("\n".join(
            wrap(tarot_cards.information_guide["court_cards"], self.line_size)) + "\n")
        self.draw_line()
        sleep(1)
        print("\033[1m" + "About the Suits cards".ljust(self.line_size) + "\033[0m" + '\n')
        print("\n".join(
            wrap(tarot_cards.information_guide["groups"], self.line_size)) + "\n")
        self.draw_line()
        sleep(1)
        print("\033[1m" + "About Neighbor cards".ljust(self.line_size) + "\033[0m" + '\n')
        print("\n".join(
            wrap(tarot_cards.information_guide["neighbor_cards"], self.line_size)) + "\n")
        sleep(1)

    def show_dominant_cards(self):
        self.draw_line()
        print("\033[1m" + "DOMINANT CARDS".ljust(self.line_size) +
              "\033[0m" + '\n')
        print("\n".join(
            wrap(tarot_cards.information_guide["dominant"], self.line_size)) + "\n")
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
        print(
            "\033[1m" + "CARDS UPPER RIGHT".ljust(self.line_size) + "\033[0m" + '\n')
        print("\n".join(
            wrap(tarot_cards.information_guide["potential_right"], self.line_size)) + "\n")
        for card in self.potential_cards__upper_right:
            number += 4
            self.draw_card()
            print(
                "+" + f"Card nº {number}: {card['name']}".center(self.card_size - 2) + "+")
            self.draw_card_line()
            print("\n".join(wrap(card["meaning"], self.card_size)) + "\n")

    def show_pontetial_cards_upper_left(self):
        number = 1
        self.draw_line()
        print(
            "\033[1m" + "CARDS UPPER LEFT".ljust(self.line_size) + "\033[0m" + '\n')
        print("\n".join(
            wrap(tarot_cards.information_guide["potential_left"], self.line_size)) + "\n")
        for card in self.potential_cards_upper_left:
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
        print("\033[1m" + "ASSISTANT CARDS".ljust(self.line_size) +
              "\033[0m" + '\n')
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
        print("\033[1m" + "DESTINY CARDS".ljust(self.line_size) +
              "\033[0m" + '\n')
        print("\n".join(
            wrap(tarot_cards.information_guide["destiny_cards"], self.line_size)) + "\n")
        for card in self.destiny_cards:
            number += 4
            self.draw_card()
            print(
                "+" + f"Card nº {number}: {card['name']}".center(self.card_size - 2) + "+")
            self.draw_card_line()
            print("\n".join(wrap(card["meaning"], self.card_size)) + "\n")

    def start_tarot(self):
        self.draw_line()
        print(
            "\033[1m" + "TARO DIVINATION DARK MAGICK".center(self.line_size) + "\033[0m")
        self.draw_line()
        print("\n".join(wrap("Welcome to our TAROT divination system. This system is true to " +
              "\033[1m" + "ALEISTER CROWLEY " + "\033[0m" + "TAROT system.", self.line_size)))
        self.draw_line()
        tarot.fillDeck()
        tarot.get_name()
        tarot.get_factor()
        tarot.shuffle_deck()
        tarot.draw_fifteen()
        tarot.show_instructions()
        tarot.show_dominant_cards()
        sleep(1)
        tarot.show_potential_cards_upper_right()
        sleep(1)
        tarot.show_pontetial_cards_upper_left()
        sleep(1)
        tarot.show_assist_cards()
        sleep(1)
        tarot.show_destiny_cards()
        sleep(1)
        tarot.closing_invocation()

    def save(self):
        self.save = input("\n".join(wrap(f"Master {self.get_last_name()}, would you like to save this to your personal archieve? (Yes or No)", self.line_size)) + "\n")
        if self.save == "Yes":
            with open(f"{self.get_last_name()} - {self.current_date} - {self.factor}.txt", "w") as saved_file:
                saved_file.write(

                    f"{self.name}\n"
                    "----------------------\n"
                    f"{self.current_date}\n"
                    "----------------------\n"
                    f"{self.factor}\n"
                    "----------------------\n"
                    f"Card 01 - {self.dominant_cards[0]['name']}\n"
                    f"{self.dominant_cards[0]['meaning']}\n"
                    "----------------------\n"
                    f"Card 02 - {self.dominant_cards[1]['name']}\n"
                    f"{self.dominant_cards[1]['meaning']}\n"
                    "----------------------\n"
                    f"Card 03 - {self.dominant_cards[2]['name']}\n"
                    f"{self.dominant_cards[2]['meaning']}\n"
                    "----------------------\n"
                    f"Card 04 - {self.potential_cards__upper_right[0]['name']}\n"
                    f"{self.potential_cards__upper_right[0]['meaning']}\n"
                    "----------------------\n"
                    f"Card 08 - {self.potential_cards__upper_right[1]['name']}\n"
                    f"{self.potential_cards__upper_right[1]['meaning']}\n"
                    "----------------------\n"
                    f"Card 12 - {self.potential_cards__upper_right[2]['name']}\n"
                    f"{self.potential_cards__upper_right[2]['meaning']}\n"
                    "----------------------\n"
                    f"Card 05 - {self.potential_cards_upper_left[0]['name']}\n"
                    f"{self.potential_cards_upper_left[0]['meaning']}\n"
                    "----------------------\n"
                    f"Card 09 - {self.potential_cards_upper_left[1]['name']}\n"
                    f"{self.potential_cards_upper_left[1]['meaning']}\n"
                    "----------------------\n"
                    f"Card 13 - {self.potential_cards_upper_left[2]['name']}\n"
                    f"{self.potential_cards_upper_left[2]['meaning']}\n"
                    "----------------------\n"
                    f"Card 06 - {self.assist_cards[0]['name']}\n"
                    f"{self.assist_cards[0]['meaning']}\n"
                    "----------------------\n"
                    f"Card 10 - {self.assist_cards[1]['name']}\n"
                    f"{self.assist_cards[1]['meaning']}\n"
                    "----------------------\n"
                    f"Card 14 - {self.assist_cards[2]['name']}\n"
                    f"{self.assist_cards[2]['meaning']}\n"
                    "----------------------\n"
                    f"Card 07 - {self.destiny_cards[0]['name']}\n"
                    f"{self.destiny_cards[0]['meaning']}\n"
                    "----------------------\n"
                    f"Card 11 - {self.destiny_cards[1]['name']}\n"
                    f"{self.destiny_cards[1]['meaning']}\n"
                    "----------------------\n"
                    f"Card 15 - {self.destiny_cards[2]['name']}\n"
                    f"{self.destiny_cards[2]['meaning']}\n"
                )


tarot = Tarot()
tarot.start_tarot()
tarot.save()
