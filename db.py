FILENAME = "Money.txt"

def writeMoney(payOut):
    try:
        with open (FILENAME, "w", newline = "") as file:
            file.write(str(payOut))
    except Exception as e:
        print(type(e), e)

def readMoney():
    try:
        money = []
        with open(FILENAME, "r", newline = "") as file:
            money = file.readline()
            money.append(money)
            print("Money:\t" + money[0][0])
            return float(money[0][0])
    except FileNotFoundError:
        print("Could not find the file. try again")
    except Exception as e:
        print(type(e), e)