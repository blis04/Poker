import playingcards

hand_types = ['high card', 'one pair', 'two pair', 'three of a kind', 'straight', 'flush', 'full house', 'four of a kind', 'straight flush']

d = playingcards.Deck()
d.shuffle()

ph1 = playingcards.PokerHand()
ph2 = playingcards.PokerHand()

# do this 5 times
for _ in range(5):
    # deal 1 card each to each player
    ph1.add_to_hand(d.deal())
    ph2.add_to_hand(d.deal())


print('Player 1 hand:', str(ph1))
hand1_val = ph1.determine_hand() # will return a # 0 .. 8
print('Player 1 has a', hand_types[hand1_val])
print('Player 2 hand:', str(ph2))
hand2_val = ph2.determine_hand() # will return a # 0 .. 8
print('Player 2 has a', hand_types[hand2_val])

highCardCount = 0
onePairCount = 0
twoPairCount = 0
threeKindCount = 0
straightCount = 0
flushCount = 0
fullHouseCount = 0
fourKindCount = 0
straighflushCount = 0
for _ in range(200000):
    ph1 = playingcards.PokerHand()
    ph2 = playingcards.PokerHand()
    d = playingcards.Deck()
    d.shuffle()
    for _ in range(5):
        # deal 1 card each to each player
        ph1.add_to_hand(d.deal())
        ph2.add_to_hand(d.deal())
    ###determines the hand that was just dealth
    hand1_val = ph1.determine_hand()
    hand2_val= ph2.determine_hand()
    #print(hand1_val,hand2_val)
    if hand1_val == 0:
        highCardCount += 1

    if hand2_val == 0:
        highCardCount += 1

    elif hand1_val == 1:
        onePairCount += 1
    elif hand2_val == 1:
        onePairCount += 1
    elif hand1_val == 2:
        twoPairCount += 1
    elif hand2_val == 2:
        twoPairCount += 1
    elif hand1_val == 3:
        threeKindCount += 1
    elif hand2_val == 3:
        threeKindCount += 1
    elif hand1_val == 4:
        straightCount += 1
    elif hand2_val == 4:
        straightCount += 1
    elif hand1_val == 5:
        flushCount += 1
    elif hand2_val == 5:
        flushCount += 1
    elif hand1_val == 6:
        fullHouseCount += 1
    elif hand2_val == 6:
        fullHouseCount += 1
    elif hand1_val == 7:
         fourKindCount+= 1
    elif hand2_val == 7:
        fourKindCount += 1
    elif hand1_val == 8:
        straighflushCount += 1
    elif hand2_val == 8:
        straighflushCount +=1
divisor = 400000
print(f'The number of high card hands was {highCardCount}, which is a probability of {highCardCount/divisor} to 1.')
print(f'The number of one pair hands was {onePairCount}, which is a probability of {onePairCount/divisor} to 1.')
print(f'The number of two pair hands was {twoPairCount}, which is a probability of {twoPairCount/divisor} to 1.')
print(f'The number of three of a kind hands was {threeKindCount}, which is a probability of {threeKindCount/divisor} to 1.')
print(f'The number of straight hands was {straightCount}, which is a probability of {straightCount/divisor} to 1.')
print(f'The number of flush hands was {flushCount}, which is a probability of {flushCount/divisor} to 1.')
print(f'The number of full house hands was {fullHouseCount}, which is a probability of {fullHouseCount/divisor} to 1.')
print(f'The number of four of a kind hands was {fourKindCount}, which is a probability of {fourKindCount/divisor} to 1.')
print(f'The number of straight flush hands was {straighflushCount}, which is a probability of {straighflushCount/divisor} to 1.')


