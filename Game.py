import CardGameHandler as Handler

playing = True


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Bet chips: "))
        except:
            print("Sorry, please provide proper number")
        else:
            if chips.bet > chips.total:
                print("Sorry, you dont have enough chips. You have only: {}".format(chips.total))
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_aces()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("Hit or Stand? Enter h or s: ")
        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player stands Dealer's turn.")
            playing = False
        else:
            print("Please enter h or s only")
            continue
        break

    return playing


def show_some(player, dealer):
    print("\nDEALERS HAND: ")
    print("One card hidden!")
    print(dealer.cards[1])
    print("\n")
    print("PLAYERS HAND: ")
    for card in player.cards:
        print(card)
    print("Value:", player.value)


def show_all(player, dealer):
    print("\nDEALERS HAND: ")
    for card in dealer.cards:
        print(card)
    print("DEALERS Value:", dealer.value)

    print("\n")
    print("PLAYERS HAND: ")
    for card in player.cards:
        print(card)
    print("PLAYERS Value:", player.value)


def player_bust(chips):
    chips.lose_bet()
    print("Player Busted!")


def player_win(chips):
    chips.win_bet()
    print("Player Won!")


def dealer_bust(chips):
    chips.win_bet()
    print("Dealer Busted! Player Wins")


def dealer_win(chips):
    chips.lose_bet()
    print("Dealer Won!")


def push():
    print("Dealer and Player tie! It's a push.")


# Start the game code
print("Welcome to Black Jack!!!\n")
# Set up player chips
player_chips = Handler.Chips(1000)

while True:
    print("====================================  Starting Game  ==============================")

    # Create and shuffle deck and deal 2 cards each
    deck = Handler.Deck()
    deck.shuffle()

    player_hand = Handler.Hand()
    dealer_hand = Handler.Hand()

    for _ in range(2):
        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

    # Prompt the player for their bet
    take_bet(player_chips)

    # Show some cards
    show_some(player_hand, dealer_hand)

    while playing:

        hit_or_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_bust(player_chips)
            show_all(player_hand, dealer_hand)
            break

    # if player hasn't busted
    if player_hand.value <= 21:

        while dealer_hand.value < player_hand.value:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        # run winning scenarios
        if dealer_hand.value > 21:
            dealer_bust(player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_win(player_chips)
        elif dealer_hand.value < player_hand.value:
            player_win(player_chips)
        else:
            push()

    print("\nPlayer's winnings stand at", player_chips.total)

    if player_chips.total > 0:
        # Ask to play again
        new_game = input("Would you like to play another hand? Enter 'y' or 'n': ")
        if new_game[0].lower() == 'y':
            playing = True
            continue
    else:
        print("Thanks for playing!")
        break
