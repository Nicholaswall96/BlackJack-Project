import random
import sys
import db


def displayTitle():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2\n")


def playGame(deck):
    #Dealers hand
    dealerHand = []
    dealerHandValue = 0
    while True:
        if dealerHandValue < 17:
            dealCard = random.randint(0, len(deck) - 1)
            dealerCard = deck[dealCard]
            dealerHand.append(dealerCard)
            dealerHandValue = 0
            for card in dealerHand:
                dealerHandValue += int(card[2])
        elif dealerHandValue >= 17:
            break
    print("\nDEALER'S SHOW CARD:")
    print(dealerHand[0][0], "of", dealerHand[0][1])

    # This shows the players hand and if they want to hit/stand
    playerHand = []
    playerHandValue = 0
    i = 0
    while i < 2:
        dealCard = random.randint(0, len(deck) - 1)
        playerCard = deck[dealCard]
        playerHand.append(playerCard)
        i += 1
    print("\nYOUR CARDS:")
    for card in playerHand:
        print(card[0], "of", card[1])
        playerHandValue += int(card[2])
    playerChoice = input("\nHit or Stand? (hit/stand):  ")

    # If hit, loops through to check if its under 21, if true, gives option to hit or stand again
    # if hit and over 21 it breaks
    # if stand it breaks
    while True:
        try:
            if playerChoice.lower() == "hit":
                dealCard = random.randint(0, len(deck) - 1)
                playerCard = deck[dealCard]
                playerHand.append(playerCard)

                print("\nYOUR CARDS:")
                playerHandValue = 0
                for card in playerHand:
                    print(card[0], "of", card[1])
                    playerHandValue += int(card[2])
                if playerHandValue > 21:
                    break
                else:
                    playerChoice = input("\nHit or Stand? (hit/stand):  ")
            elif playerChoice.lower() == "stand":
                break
            else:
                print("Not valid Entry")
                playerChoice = input("\nHit or Stand? (hit/stand):  ")
        except ValueError:
            print("Invalid Entry")
        except Exception as e:
            print("Unexpected error ", type(e), e)
            sys.exit(1)

    print("\nDEALER'S CARDS: ")
    for card in dealerHand:
        print(f"{card[0]} of {card[1]}")

    print(f"\nYOUR POINTS:\t{playerHandValue}")
    print(f"DEALER'S POINTS:\t{dealerHandValue}")


# Determines who wins with various if and statements
    playerWins = 0
    if playerHandValue > 21:
        print("\nYou bust! You lose your bet")
        return playerWins
    elif playerHandValue <= 21 and playerHandValue > dealerHandValue:
        print("\nCongrats! you win your bet")
        playerWins = 1
        return playerWins
    elif dealerHandValue <= 21 and dealerHandValue > playerHandValue:
        print("\nSorry! You lose.")
        return playerWins
    elif dealerHandValue > 21 and playerHandValue <= 21:
        print("\nDealer busts! You win your bet")
        playerWins = 1
        return playerWins
    elif playerHandValue <= 21 and playerHandValue == dealerHandValue:
        print("\nA standoff! You get your bet back")
        playerWins = 2
        return playerWins


def main():
    # main deck
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
    choice = "y"
    while choice.lower() == "y":
        MoneyAmount = db.readMoney()
        betAmount = float(input("Bet amount: "))
        while betAmount < 5 or betAmount > 1000:
            print("You cannot bet less than $5 or more than $1000.")
            betAmount = float(input("Bet amount: "))
        while betAmount > MoneyAmount:
            print("You cannot bet more than what you have.")
            betAmount = float(input("Bet amount: "))

        playerWins = playGame(deck)
        if playerWins == 1:
            payOut = round((betAmount * 1.5) + MoneyAmount, 2)
            print(f"\nMoney: {payOut}")
        elif playerWins == 2:
            payOut = round(betAmount+ MoneyAmount, 2)
            print(f"\nMoney: {payOut}")
        else:
            payOut = round(betAmount - (2 * betAmount) + MoneyAmount, 2)
            print(f"\nMoney: {payOut}")
        if payOut < 5:
            print("\nYou must buy more chips to continue")
            payOut = float(input("Enter number of chips you want to buy: "))

        payOut = str(payOut)
        db.writeMoney(payOut)
        choice = input("\nPlay again? (y/n): \n")
    print("\nCome back soon!")
    print("Bye")

if __name__ == "__main__":
    main()
