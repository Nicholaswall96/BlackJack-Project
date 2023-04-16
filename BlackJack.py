import random
import sys

#Title
def displayTitle():
    print("BLACKJACK! Play Responsibly")
    print("Blackjack payout is 3:2\n")

def gamePlay(cardDeck):
    #This shows the dealers hand
    dealerHand = []
    dealerHandValue = 0
    while True:
        if dealerHandValue < 17:
            dealCard = random.randint(0, len(cardDeck) - 1)
            dealerCard = cardDeck[dealCard]
            dealerHand.append(dealerCard)
            dealerHandValue = 0
            for card in dealerHand:
                dealerHandValue += int(card[2])
        elif dealerHandValue >= 17:
            break
    print("\nDealer show card:")
    print(f"{dealerHand[0][0]} of {dealerHand[0][1]}")

    #This shows the players hand and if they want to hit/stand
    playerHand = []
    playerHandValue = 0
    i = 0
    while i < 2:
        dealCard = random.randint(0, len(cardDeck) - 1)
        playerCard = cardDeck[dealCard]
        playerHand.append(playerCard)
        i += 1
    print("\nPLAYER'S CARDS:")
    for card in playerHand:
        print(card[0], "of", card[1])
        playerHandValue += int(card[2])
    playerChoice = input("\nHit or Stand? (Hit/Stand):  ")

    #If hit, loops through to check if its under 21, if true, gives option to hit or stand again
    #if hit and over 21 it breaks
    #if stand it breaks
    while True:
        try:
            if playerChoice.lower() == "Hit":
                dealCard = random.randint(0, len(cardDeck)-1)
                playerCard = cardDeck[dealCard]
                playerHand.append(playerCard)

                print("\nYour hand is: ")
                playerHandValue = 0
                for card in playerHand:
                    print(f"{card[0]} of {card[1]}")
                    playerHandValue += int(card[2])
                if playerHandValue > 21:
                    break
                else:
                    playerChoice = input("\nHit or Stand? (Hit/Stand): ")
            elif playerChoice.lower() == "Stand":
                break
            else:
                print("You must say Hit or Stand")
                playerChoice = input("\nHit or Stand? (Hit/Stand): ")
        except ValueError:
            print("Invalid Entry")
        except Exception as e:
            print("Unexpected error ", type(e), e)
            sys.exit(1)




def main():
    deck = [["2", "Spades", 2], ["2", "Clubs", 2], ["2", "Diamonds", 2], ["2", "Hearts", 2],
            ["3", "Spades", 3], ["3", "Clubs", 3], ["3", "Diamonds", 3], ["3", "Hearts", 3],
            ["4", "Spades", 4], ["4", "Clubs", 4], ["4", "Diamonds", 4], ["4", "Hearts", 4],
            ["5", "Spades", 5], ["5", "Clubs", 5], ["5", "Diamonds", 5], ["5", "Hearts", 5],
            ["6", "Spades", 6], ["6", "Clubs", 6], ["6", "Diamonds", 6], ["6", "Hearts", 6],
            ["7", "Spades", 7], ["7", "Clubs", 7], ["7", "Diamonds", 7], ["7", "Hearts", 7],
            ["8", "Spades", 8], ["8", "Clubs", 8], ["8", "Diamonds", 8], ["8", "Hearts", 8],
            ["9", "Spades", 9], ["9", "Clubs", 9], ["9", "Diamonds", 9], ["9", "Hearts", 9],
            ["10", "Spades", 10], ["10", "Clubs", 10], ["10", "Diamonds", 10], ["10", "Hearts", 10],
            ["Jack", "Spades", 10], ["Jack", "Clubs", 10], ["Jack", "Diamonds", 10], ["Jack", "Hearts", 10],
            ["Queen", "Spades", 10], ["Queen", "Clubs", 10], ["Queen", "Diamonds", 10], ["Queen", "Hearts", 10],
            ["King", "Spades", 10], ["King", "Clubs", 10], ["King", "Diamonds", 10], ["King", "Hearts", 10],
            ["Ace", "Spades", 1, 11], ["Ace", "Clubs", 1, 11], ["Ace", "Diamonds", 1, 11], ["Ace", "Hearts", 1, 11]]
    displayTitle()


if __name__ == "__main__":
    main()