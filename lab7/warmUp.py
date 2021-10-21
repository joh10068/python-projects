
warmUp = "mississippi"

numberS = warmUp.count('s')

replaceOx = warmUp.replace('iss', 'ox')

indexP = warmUp.index('p')



def foo(istring):
    p = '0123456789'
    os = ''
    for iterator in istring:
        if iterator not in p:
            os += iterator
    return os


def multiLetter(word):
    wordString = word
    firstLetter = wordString[0]
    letterCount = wordString.count(firstLetter)
    if letterCount > 1:
        return True
    if letterCount == 1:
        return False
    
def wordListChecker():
    multiLetterList = []
    wordList = []
    inclusionList = 'abcdefghijklmnopqrstuvwxyz'
    ValidWord = True
    wordTest = True
    
    while ValidWord == True:
        newWord = input("Enter a word:")
        for i in newWord:
            if i not in inclusionList:
                wordTest = False
        if (newWord == '') or (wordTest == False):
            ValidWord = False
        else:
            wordList.append(newWord)

    for i in range(len(wordList)):
        checkWord = multiLetter(wordList[i])
        if checkWord == True:
            multiLetterList.append(wordList[i])
    print (multiLetterList)
        


def is_palindrome(word):
    testString = word.lower()
    for i in testString:
        letter = i
        letterCheck = letter.isalpha()
        if letterCheck == False:
            testString = testString.replace(str(letter),'')
    stringLength = len(testString)-1
    
    for n in range(len(testString)):
        firstLetterIndex = n
        lastLetterIndex = stringLength - n
        if firstLetterIndex == lastLetterIndex:
            break
        firstLetter = testString[n]
        lastLetter = testString[lastLetterIndex]
        if firstLetter == lastLetter:
            palindromeCheck = True
        else:
            palindromeCheck = False
            break

    print(palindromeCheck)
        
        
    
def mysplit(stringarg, delimiter):
    endOfString = (len(stringarg)-1)
    delimitIndexList = [0]
    delimitIndex = -1
    splitList = []
    
    while True:
        delimitIndex = stringarg.find(delimiter, delimitIndex+1)
        if delimitIndex == -1:
            break
        delimitIndexList.append(delimitIndex)

    stringarg = stringarg.replace(delimiter,'')

    for i in range(len(delimitIndexList)-1):
        firstIndex = delimitIndexList[i]
        secondIndex = delimitIndexList[i+1]
        newString = stringarg[firstIndex:secondIndex]
        splitList.append(newString)

    print(splitList)


def DNA_gene_reader():
    start_codon = 'ATG'
    stop_codon = ['TAG', 'TAA', 'TGA']

    validGene = True
    gene_list = []
    
    DNA_sequence = input("ENTER DNA SEQUENCE:")

    startDNAsplit = DNA_sequence.split('ATG')

    for i in range(len(startDNAsplit)):
        for n in range(3):
            if stop_codon[n] in startDNAsplit[i]:
                newGene = startDNAsplit[i].split(stop_codon[n])
                for m in range(3):
                    if stop_codon[m] in newGene[0]:
                        validGene = False
                        break
                    else:
                        validGene = True
                if validGene == True:
                    gene_list.append(newGene[0])
                        
                    
    for g in range(len(gene_list)):
        print("GENE #" + str(g) + " is: " + gene_list[g])
    

def bjscore(string):
    tenPts = 'TJQK'
    faceValue = '23456789'
    ace = 'A'
    score = 0
    
    for i in string:
        if i in tenPts:
            score += 10
        elif i in faceValue:
            pts = int(i)
            score += pts
        elif i in ace:
            if score <= 10:
                score += 11
            elif score > 10:
                score += 1

##    if score > 21:
##        print ("you busted your nut")
##    else:
##        print (score)
##    print (score)
    return score

import random

def dealerBJ(numberHands):
    deck = ['2','2','2','2','3','3','3','3',
            '4','4','4','4','5','5','5','5',
            '6','6','6','6','7','7','7','7',
            '8','8','8','8','9','9','9','9',
            'T','T','T','T','J','J','J','J',
            'Q','Q','Q','Q','K','K','K','K',
            'A','A','A','A']
    hand_history = []
    score_history = []
    newDeck = deck[0:51]
    random.shuffle(newDeck)
    
    for i in range(numberHands):
        active_deal = True
        current_hand = ""
        while active_deal == True:
            current_hand += str(newDeck[0])
            newDeck.pop(0)
            current_score = bjscore(current_hand)
##            print(current_hand)
##            print(newDeck)
            if current_score >= 17 and current_score <= 21:
                hand_history.append(current_hand)
                score_history.append(current_score)
                active_deal = False
            if current_score > 21:
                hand_history.append(current_hand)
                score_history.append("busted")
                active_deal = False
            if len(newDeck) == 0:
                newDeck = deck[0:51]
                random.shuffle(newDeck)

    numberBusted = round(score_history.count("busted")/numberHands * 100, 2)
    number17 = round(score_history.count(17)/numberHands * 100, 2)
    number18 = round(score_history.count(18)/numberHands * 100, 2)
    number19 = round(score_history.count(19)/numberHands * 100, 2)
    number20 = round(score_history.count(20)/numberHands * 100, 2)
    number21 = round(score_history.count(21)/numberHands * 100, 2)

    print("bust %: " + str(numberBusted))
    print("17 %: " + str(number17)) 
    print("18 %: " + str(number18))
    print("19 %: " + str(number19))
    print("20 %: " + str(number20))
    print("21 %: " + str(number21))
##    print (hand_history)

    
##bjscore('A7') 
dealerBJ(1000000)


    
