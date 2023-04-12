FILENAME = "Money.txt"

def writeMoney(payOut):
    try:
        with open (FILENAME, "w", newline = "") as file:
            file.write(str(payOut))
    except Exception as e:
        print(type(e), e)

def readMoney():
    try:
        moneyAmount = []
        with open(FILENAME, "r", newline = "") as file:
            money = file.readline()
            moneyAmount.append(money)
            print("Money:\t" + moneyAmount[0][0])
            return float(moneyAmount[0][0])
    except FileNotFoundError:
        print("Could not find the file. try again")
    except Exception as e:
        print(type(e), e)