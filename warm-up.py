import turtle
import random

def random_list(n):
    randomList = []
    for i in range(n):
        newItem = random.randint(1,n)
        randomList.append(newItem)
    return (randomList)
        
def find_min(vals):
    savedValue = vals[0]
    for i in range(len(vals)):
        if savedValue > vals[i]:
            savedValue = vals[i]
            indexValue = i
    return (indexValue)

def swap_min(vals):
    ticker = 0
    newIndex = find_min(vals)
    swapValue = vals[ticker]
    minValue = vals[newIndex]
    vals.pop(ticker)
    vals.insert(ticker,minValue)
    vals.insert(newIndex,swapValue)
    vals.pop(newIndex+1)
    return vals
    
def get_list():
    wordList = []
    runAppend = True
    while runAppend is True:
        print('Enter word:')
        userInput = input()
        if userInput == '':
            runAppend = False
            break
        wordList.append(userInput)
    return wordList
    
def union(set1, set2):
    masterSet = set2
    for i in range(len(set1)):
        for n in range(len(set2)):
            if set1[i] == set2[n]:
                break
            else:
                masterSet.append(set1[i])
                break
    return masterSet


def turtle_race(turtles):
    turtleList = []
    turtleSelection = 0
    turtleMovement = 0
    turtleColors = ["blue","red","green","cyan","magenta","yellow","black"]
    turtle.setworldcoordinates(0,0,500,500)
    winner = False
    for i in range(turtles):
        randomTurtle = turtle.Turtle()
        randomTurtle.penup()
        randomTurtle.speed(0)
        randomTurtle.setpos(0,random.randint(0,500))
        randomTurtle.shape("turtle")
        randomColor = turtleColors[random.randint(0,6)]
        randomTurtle.color(randomColor)
        randomTurtle.pendown()
        turtleList.append(randomTurtle)
    while winner == False:
        turtleSelection = random.randint(0,(turtles-1))
        turtleMovement = random.randint(1,50)
        turtleSelected = turtleList[turtleSelection]
        turtleSelected.forward(turtleMovement)
        turtlePosition = turtleSelected.xcor()
        if turtlePosition >= 450:
            turtleSelected.turtlesize(5)
            winnerString = str("Turtle #" + str(turtleSelection) + " wins!")
            winnerPrint = turtle.Turtle()
            winnerPrint.penup()
            winnerPrint.setpos(250,250)
            winnerPrint.write(winnerString, align="center")
            winnerPrint.ht()
            winner = True

turtle_race(1000)

def selection_sort(numberLength):
    ticker = 0
    newList = random_list(numberLength)
    for i in range(len(newList)):
        swapValue = newList[i]
        
        
        
    
    
        
        
        






        
    
