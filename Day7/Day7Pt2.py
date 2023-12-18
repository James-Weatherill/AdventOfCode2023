#! /opt/homebrew/bin/python3

from time import time

startTime = time()

########################################

fixedList = []
file1 = open("input.txt", "r")
file2 = open("testInput.txt", "r")
fileReadStr = str(file1.readlines()).replace("\\n", "").replace(", ", ",").replace("'", "").replace("[", "").replace("]", "").split(",")
for item in fileReadStr:
    fixedList.append(item.split(" "))
for i in range(len(fixedList)):
    fixedList[i][0] = list(fixedList[i][0])
for i in range(len(fixedList)):
    for j in range(len(fixedList[i][0])):
        if fixedList[i][0][j] == "T":
            fixedList[i][0][j] = "10"
        if fixedList[i][0][j] == "J":
            fixedList[i][0][j] = "1"
        if fixedList[i][0][j] == "Q":
            fixedList[i][0][j] = "12"
        if fixedList[i][0][j] == "K":
            fixedList[i][0][j] = "13"
        if fixedList[i][0][j] == "A":
            fixedList[i][0][j] = "14"
        if fixedList[i][0][j] != "J":
            fixedList[i][0][j] = int(fixedList[i][0][j])
for i in range(len(fixedList)):
    fixedList[i][1] = int(fixedList[i][1])

########################################

counter = len(fixedList)+1
ans = 0

numberOfFiveOfAKind = []
numberOfFourOfAKind = []
numberOfFullHouses = []
numberOfThreeOfAKind = []
numberOfTwoPairs = []
numberOfOnePairs = []
numberOfHighCards = []

def fiveOfAKind(inputHand):
    tempSet = set()
    for card in inputHand:
        tempSet.add(card)
    if len(tempSet)==1:
        return True
    else:
        return False

def fourOfAKind(inputHand):
    oneCount = 0
    twoCount = 0
    threeCount = 0
    fourCount = 0
    fiveCount = 0
    sixCount = 0
    sevenCount = 0
    eightCount = 0
    nineCount = 0
    tenCount = 0
    jackCount = 0
    queenCount = 0
    kingCount = 0
    aceCount = 0
    tempSet = set()
    for card in inputHand:
        tempSet.add(card)
        if card == 1:
            oneCount += 1
        elif card == 2:
            twoCount += 1
        elif card == 3:
            threeCount += 1
        elif card == 4:
            fourCount += 1
        elif card == 5:
            fiveCount += 1
        elif card == 6:
            sixCount += 1
        elif card == 7:
            sevenCount += 1
        elif card == 8:
            eightCount += 1
        elif card == 9:
            nineCount += 1
        elif card == 10:
            tenCount += 1
        elif card == 11:
            jackCount += 1
        elif card == 12:
            queenCount += 1
        elif card == 13:
            kingCount += 1
        elif card == 14:
            aceCount += 1
    if len(tempSet)==2:
        if oneCount==4 or twoCount==4 or threeCount==4 or fourCount==4 or fiveCount==4 or sixCount==4 or sevenCount==4 or eightCount==4 or nineCount==4 or tenCount==4 or jackCount==4 or queenCount==4 or kingCount==4 or aceCount==4:
            return True
        else:
            return False

def fullHouse(inputHand):
    tempSet = set()
    for card in inputHand:
        tempSet.add(card)
    if len(tempSet)==2:
        return True
    else:
        return False

def threeOfAKind(inputHand):
    oneCount = 0
    twoCount = 0
    threeCount = 0
    fourCount = 0
    fiveCount = 0
    sixCount = 0
    sevenCount = 0
    eightCount = 0
    nineCount = 0
    tenCount = 0
    jackCount = 0
    queenCount = 0
    kingCount = 0
    aceCount = 0
    numberOfPairs = 0
    tempSet = set()
    for card in inputHand:
        tempSet.add(card)
        if card == 1:
            oneCount += 1
        elif card == 2:
            twoCount += 1
        elif card == 3:
            threeCount += 1
        elif card == 4:
            fourCount += 1
        elif card == 5:
            fiveCount += 1
        elif card == 6:
            sixCount += 1
        elif card == 7:
            sevenCount += 1
        elif card == 8:
            eightCount += 1
        elif card == 9:
            nineCount += 1
        elif card == 10:
            tenCount += 1
        elif card == 11:
            jackCount += 1
        elif card == 12:
            queenCount += 1
        elif card == 13:
            kingCount += 1
        elif card == 14:
            aceCount += 1
    tempList = [oneCount, twoCount, threeCount, fourCount, fiveCount, sixCount, sevenCount, eightCount, nineCount, tenCount, jackCount, queenCount, kingCount, aceCount]
    for lst in tempList:
        if lst == 2:
            numberOfPairs += 1
    if len(tempSet)==3:
        if numberOfPairs == 0:
            return True
        else:
            return False

def twoPair(inputHand):
    tempSet = set()
    for card in inputHand:
        tempSet.add(card)
    if len(tempSet)==3:
        return True
    else:
        return False

def onePair(inputHand):
    tempSet = set()
    for card in inputHand:
        tempSet.add(card)
    if len(tempSet)==4:
        return True
    else:
        return False

for i in range(len(fixedList)):
    if fiveOfAKind(fixedList[i][0]):
        fixedList[i].append("five")
    elif fourOfAKind(fixedList[i][0]):
        fixedList[i].append("four")
    elif fullHouse(fixedList[i][0]):
        fixedList[i].append("full")
    elif threeOfAKind(fixedList[i][0]):
        fixedList[i].append("three")
    elif twoPair(fixedList[i][0]):
        fixedList[i].append("two")
    elif onePair(fixedList[i][0]):
        fixedList[i].append("one")
    else:
        fixedList[i].append("high")

for i in range(len(fixedList)):
    numberOfJokers = 0
    for j in range(len(fixedList[i][0])):
        if fixedList[i][0][j] == 1:
            numberOfJokers += 1
    if (numberOfJokers == 1 and fixedList[i][2] == "four") or (numberOfJokers == 4 and fixedList[i][2] == "four") or (numberOfJokers == 2 and fixedList[i][2] == "full") or (numberOfJokers == 3 and fixedList[i][2] == "full"):
        fixedList[i][2] = "five"
    elif (numberOfJokers == 3 and fixedList[i][2] == "three") or (numberOfJokers == 1 and fixedList[i][2] == "three") or (numberOfJokers == 2 and fixedList[i][2] == "two"):
        fixedList[i][2] = "four"
    elif (numberOfJokers == 1 and fixedList[i][2] == "two"):
        fixedList[i][2] = "full"
    elif (numberOfJokers == 1 and fixedList[i][2] == "one") or (numberOfJokers == 2 and fixedList[i][2] == "one"):
        fixedList[i][2] = "three"
    elif (numberOfJokers == 1 and fixedList[i][2] == "high"):
        fixedList[i][2] = "one"

for lst in fixedList:
    if lst[2] == "five":
        numberOfFiveOfAKind.append(lst)
    elif lst[2] == "four":
        numberOfFourOfAKind.append(lst)
    elif lst[2] == "full":
        numberOfFullHouses.append(lst)
    elif lst[2] == "three":
        numberOfThreeOfAKind.append(lst)
    elif lst[2] == "two":
        numberOfTwoPairs.append(lst)
    elif lst[2] == "one":
        numberOfOnePairs.append(lst)
    else:
        numberOfHighCards.append(lst)

numberOfFiveOfAKind = sorted(numberOfFiveOfAKind)[::-1]
numberOfFourOfAKind = sorted(numberOfFourOfAKind)[::-1]
numberOfFullHouses = sorted(numberOfFullHouses)[::-1]
numberOfThreeOfAKind = sorted(numberOfThreeOfAKind)[::-1]
numberOfTwoPairs = sorted(numberOfTwoPairs)[::-1]
numberOfOnePairs = sorted(numberOfOnePairs)[::-1]
numberOfHighCards = sorted(numberOfHighCards)[::-1]

for i in range(len(numberOfFiveOfAKind)):
    counter -= 1
    ans += numberOfFiveOfAKind[i][1]*counter

for i in range(len(numberOfFourOfAKind)):
    counter -= 1
    ans += numberOfFourOfAKind[i][1]*counter

for i in range(len(numberOfFullHouses)):
    counter -= 1
    ans += numberOfFullHouses[i][1]*counter

for i in range(len(numberOfThreeOfAKind)):
    counter -= 1
    ans += numberOfThreeOfAKind[i][1]*counter

for i in range(len(numberOfTwoPairs)):
    counter -= 1
    ans += numberOfTwoPairs[i][1]*counter

for i in range(len(numberOfOnePairs)):
    counter -= 1
    ans += numberOfOnePairs[i][1]*counter

for i in range(len(numberOfHighCards)):
    counter -= 1
    ans += numberOfHighCards[i][1]*counter

print(f"\n{ans}")

########################################

finishTime = time()

print(f"\nThe code took: {finishTime-startTime} seconds, to run!")

