import random


class Card:

    # __rank is an instance variable that can be 1..13
    # __suit is an instance variable that can be 0..3, 0=Diamonds, 1=Clubs
    #                                                  2=Heart,    3=Spades

    def __init__(self, rank, suit):
        if rank >= 1 and rank <= 13:
            self.__rank = rank
        else:
            self.__rank = 2

        if suit >= 0 and suit <= 3:
            self.__suit = suit
        else:
            self.__suit = 0

    def get_rank(self):
        return self.__rank

    def get_suit(self):
        return self.__suit

    def set_rank(self, rank):
        if rank >= 1 and rank <= 13:
            self.__rank = rank

    def set_suit(self, suit):
        if suit >= 0 and suit <= 3:
            self.__suit = suit

    def __lt__(self, rhs):
        # if self.__rank < rhs.__rank:
        #    return True
        # else:
        #    return False
        return self.__rank < rhs.__rank

    def __gt__(self, rhs):
        return self.__rank > rhs.__rank

    def __str__(self):
        # Ace of Diamonds
        # 2 of Clubs
        # Jack of ____
        suit_names = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
        if self.__rank >= 2 and self.__rank <= 10:
            outstr = str(self.__rank) + ' of ' + suit_names[self.__suit]
        elif self.__rank == 1:
            outstr = 'Ace of ' + suit_names[self.__suit]
        elif self.__rank == 11:
            outstr = 'Jack of ' + suit_names[self.__suit]
        elif self.__rank == 12:
            outstr = 'Queen of ' + suit_names[self.__suit]
        else:
            outstr = 'King of ' + suit_names[self.__suit]
        return outstr


class Deck:

    # instance variable(s): list of Card objects __the_deck
    def __init__(self):
        self.__the_deck = []
        for s in range(0, 4):
            for r in range(1, 14):
                self.__the_deck.append(Card(r, s))

    # return the Card in the 0th spot of __the_deck
    # should also remove that card from the list
    # deal
    # will crash if done too many times (e.g. 53)
    def deal(self):
        return self.__the_deck.pop(0)

    # shuffle
    # assumes we only shuffle a full deck of 52 cards
    def shuffle(self):
        for _ in range(200):
            randidx = random.randint(0, 51)
            randcard = self.__the_deck.pop(randidx)
            self.__the_deck.append(randcard)

    # cut
    def cut(self):
        randidx = random.randint(0, 51)
        self.cut_at(randidx)

    def cut_at(self, placeidx):
        # pop the deck placeidx times and append them to the end
        # another idea is to use slices:
        self.__the_deck = self.__the_deck[placeidx:] + self.__the_deck[:placeidx]

    def __str__(self):

        deckstr = ''

        for c in self.__the_deck:
            deckstr += str(c) + '\n'

        return deckstr


class PokerHand:

    # self.__hand will be the instance variable that holds a list of card
    #             objects in the PokerHand

    def __init__(self):
        self.__hand = []  # just store an empty list in the instance variable
        # when an object of PokerHand is created

    def add_to_hand(self, a_card):
        if len(self.__hand) < 5:
            self.__hand.append(a_card)  # only add the card to the hand if
            # we don't have 5 cards yet

    def __str__(self):
        handstr = ''

        for c in self.__hand:
            handstr += str(c) + '\n'

        return handstr

    def determine_hand(self):
        # sort self.__hand by rank
        ranklist = []
        suitlist = []
        #card = self.__hand[0]
        #rank = Card.get_rank(card)
        #print(self.__hand[0])
        #print(rank)
        for count in range(len(self.__hand)):
            card = self.__hand[count]
            suit =card.get_suit()
            suitlist.append(suit)
            rank = card.get_rank()
            ranklist.append(rank)

        suitlist.sort()
        ranklist.sort()
        
        #flush
        if suitlist[0] == suitlist[1] and suitlist[1] == suitlist[2] and suitlist[2] == suitlist[3] and suitlist[3] == suitlist[4]:
            #straight flush
            if ranklist[0]+1 == ranklist[1] and ranklist[1]+1 == ranklist[2] and ranklist[2]+1 == ranklist[3] and ranklist[3]+1 == ranklist[4]:
                return 8
            elif ranklist[0] == 1 and ranklist[0]+1 == ranklist[1] and ranklist[1]+1 == ranklist[2] and ranklist[2]+1 == ranklist[3] and ranklist[3]+1 == ranklist[4]:
                return 8
            else:
                return 5
        #four of a kind
        elif ranklist[0] == ranklist[1] and ranklist[1] == ranklist[2] and ranklist[2] == ranklist[3]:
            return 7
        elif ranklist[1] == ranklist[2] and ranklist[2] == ranklist[3] and ranklist[3] == ranklist[4]:
            return 7
        #full house
        elif ranklist[0] == ranklist[1] and ranklist[1] == ranklist[2] and ranklist[3] == ranklist[4]:
            return 6
        elif ranklist[0] == ranklist[1] and ranklist[2] == ranklist[3] and ranklist[3] == ranklist[4]:
            return 6
        #straight
        elif ranklist[0] + 1 == ranklist[1] and ranklist[1] + 1 == ranklist[2] and \
            ranklist[2] + 1 == ranklist[3] and ranklist[3] + 1 == ranklist[4]:
            return 4
        elif ranklist[0] == 1 and ranklist[0]+1 == ranklist[1] and ranklist[1]+1 == ranklist[2] and \
            ranklist[2]+1 == ranklist[3] and ranklist[3]+1 == ranklist[4]:
            return 4
        #three of a kind
        elif ranklist[0] == ranklist[1] and ranklist[1] == ranklist[2]:
            return 3
        elif ranklist[1] == ranklist[2] and ranklist[2] == ranklist[3]:
            return 3
        elif ranklist[2] == ranklist[3] and ranklist[3] == ranklist[4]:
            return 3
        #two pair
        elif ranklist[0] == ranklist[1] and ranklist[2] == ranklist[3]:
            return 2
        elif ranklist[1] == ranklist[2] and ranklist[3] == ranklist[4]:
            return 2
        elif ranklist[0] == ranklist[1] and ranklist[3] == ranklist[4]:
            return 2
        #one pair
        elif ranklist[0] == ranklist[1]:
            return 1
        elif ranklist[1] == ranklist[2]:
            return 1
        elif ranklist[2] == ranklist[3]:
            return 1
        elif ranklist[3] == ranklist[4]:
            return 1
        else:
            return 0



        # self.__hand[0].get_rank()

       # for count in len(self.__hand):
