import random

suits = ('hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,
          'Queen':10,'King':10,'Ace':11}

playing = True


class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck():

    def __init__(self):
        self.deck = []  # START WITH EMPTY LIST

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ''

        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "the Deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


# test_deck = Deck()
# # test_deck.shuffle()
# # print(test_deck)


class Hand():

    def __init__(self):
        self.cards = []  # Start with an empty list as we did in the Deck Class
        self.value = 0   # Start with zero value
        self.aces = 0  # Add an attribute to keep track of aces

    def add_card(self,card):
        # card passed in
        # from Deck.deal() ---> single Card(suit,rank)
        self.cards.append(card)
        self.value += values[card.rank]

        # Track Aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_aces(self):

        # If total value > 21 and i still have an ace
        # Than change my ace to be a 1 instead of an 11
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


# test_deck = Deck()
# test_deck.shuffle()
#
# test_player = Hand()
#
# pulled_card = test_deck.deal()
# print(pulled_card)
# test_player.add_card(pulled_card)
#
# print(test_player.value)

# $$$$$$$$$$$$$$ CHIPS CLASS $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
class Chips():

    def __init__(self, total=100):
        self.total = 100  # This can set to a default value or support by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


# $$$$$$$$$$$$$$$$$$$$$$ take_bet CLASS   $$$$$$$$$$$$$$$$$$$$$$

def take_bet(chips):

    while True:

        try:
            chips.bet = int(input("How many chips would you like to Bet? \n"))
        except:
            print("Sorry Please enter a integer\n")
        else:

            if chips.bet > chips.total:
                print("Sorry, You dont have enough chips! You have {}".format(chips.total))
            else:
                break


def hit(deck,hand):

    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_aces()


def hit_or_stand(deck,hand):
    global playing

    while True:
        x = input("Hit or stand? Enter h or s \n")

        if x[0].lower() == 'h':
            hit(deck,hand)

        elif x[0].lower() == 's':
            print("Player stands Dealer's Turn\n")
            playing = False
        else:
            print('Sorry, I did not understand that, Please enter h or s only\n')
            continue

        break


def show_some(player, dealer):
    print("Dealer hand")
    print("One card hidden!")
    print(dealer.cards[1])
    print("\n")

    for card in player.cards:
        print(card)


def show_all(player,dealer):
    print("Dealer Hand")
    for card in dealer.cards:
        print(card)
    print("\n")
    print("Player hand")
    for card in player.cards:
        print(card)


def player_busts(player,dealer,chips):
    print("Bust Player!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(player, dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.win_bet()


def push(player,dealer):
    print("Dealer and player tie! PUSH")


# $$$$$$$$$$$$$$$$$ Game On $$$$$$$$$$$$$$$$$$$$$$$$$

while True:
    # Print an opening statement

    print("WELCOME TO BLACKJACK")
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the player's chips
    player_chips = Chips()

    # prompt the player for their bet
    take_bet(player_chips)

    # show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)

    while playing:  # Recall this variable from our hit_or_stand function
        # prompt for player to Hit or stand
        hit_or_stand(deck,player_hand)

        # show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    # If player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < player_hand.value:
            hit(deck,dealer_hand)

        # Show all cards
        show_all(player_hand,dealer_hand)

        # Run different winning scenarios

        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)

    # Inform Player of their chips and total
    print("\nPlayer Total chips are at: {}\n".format(player_chips.total))

    # Ask to Play Again
    new_game = input("Would you like to play another hand? y/s\n")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thank You for playing")
        break
































