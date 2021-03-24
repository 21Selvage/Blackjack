import random

#defining the deck of cards
def new_deck():
    return 4*('2,3,4,5,6,7,8,9,10,J,Q,K,A'.split(','))

#defining the value of each card
def card_value(card):
    return 1 if card == 'A' else 10 if card in ['J', 'Q', 'K'] else int(card)

#shuffling deck
def shuffle_deck(deck):
    random.shuffle(deck)

#givingvone card to someone
def deal_card(deck, receiverHand):
    receiverHand.append(deck.pop())

#see the biggest possible value of one's hand
def hand_value(hand):
    sum = 0
    for card in hand:
        sum += card_value(card)
    if 'A' in hand and sum < 12:
        sum += 10
    return sum

#check if it is blackjack
def is_blackjack(hand):
    return 'A' in hand and (set(hand) & {'J', 'Q', 'K'} != set())


#Main Functions
print('$$blackjack$$'.upper())
while True:
    cardsDeck = new_deck()
    shuffle_deck(cardsDeck)

    dealerHand, playerHand = [], []
    deal_card(cardsDeck, playerHand)
    deal_card(cardsDeck, dealerHand)
    deal_card(cardsDeck, playerHand)
    deal_card(cardsDeck, dealerHand)

    playerTurn = True
    while True:
        if playerTurn:
            print('Your cards are '+' '.join(playerHand)+'\nThe dealer has a {} and another card'.format(dealerHand[0]))
            if hand_value(playerHand) > 21:
                print('Busted! You lost')
                break
            elif is_blackjack(playerHand):
                playerTurn = False
                continue
            elif len(playerHand) == 5 or hand_value(playerHand) == 21:
                if len(playerHand) == 5:
                    print('5 cards!')
                if hand_value(playerHand) == 21:
                    print('21!')
                playerTurn = False
                continue
            move = input('Do you want to stand or take anothet card?\n(Enter "H" to hit or "S" to stand)\n')
            if move == 'S':
                playerTurn = False
            elif move == 'H':
                deal_card(cardsDeck, playerHand)
            else:
                print('Invalid move! Try again')
        #dealer's turn now
        else:
            print('The dealer\'s hand is '+' '.join(dealerHand))
            if hand_value(dealerHand) > 16:
                if is_blackjack(dealerHand):
                    if is_blackjack(playerHand):
                        print('You and the dealer both have Blackjack. It\'s a tie!')
                    else:
                        print('The dealer has a Blackjack. You lost!')
                elif len(playerHand) == 5:
                    print('You draw 5 cards without getting busted. You won!')
                elif hand_value(dealerHand) > hand_value(playerHand):
                    if hand_value(dealerHand) < 22:
                        print('The dealer has better cards. You lost!')
                    else:
                        print('The dealer got busted. You won!')
                elif hand_value(dealerHand) == hand_value(playerHand):
                    print('You and the dealer have the same total. It\'s a tie!')
                elif hand_value(dealerHand) < hand_value(playerHand):
                    print('You have better cards. You won!')
                break
            else:
                deal_card(cardsDeck, dealerHand)
                print('The dealer draw another card')
    move2 = input('Do you want to play another hand or leave?\n(Enter "P" to play or "L" to leave)\n')
    if move2 == 'P':
        print('Get ready for the hand\n')
        continue
    elif move2 == 'L':
        print('Thanks for playing!\n')
        break
    else: 
        print('Invalid message, too late to participate on this hand. Thanks for playing!\n')
        break
