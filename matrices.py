from math import sqrt
import turtle

def print_matrix():
    mat = []
    ls = [0,0,0,0]
    for i in range(4):
        mat.append(ls)
        mat[i][i] = 5
    print(mat)

def dist(list1,list2):
    x1=list1[0]
    y1=list1[1]
    x2=list2[0]
    y2=list2[1]
    distance2pts = sqrt(((x2-x1)**2)+((y2-y1)**2))
    return distance2pts
    #print (distance2pts)

def shortest_dist(list3):
    pointList = list3
    distanceList = []
    for i in range(len(pointList)-1): 
        for n in range(len(pointList)-1):
            if pointList[i] != pointList[n]:
                distance = dist(pointList[i],pointList[n])
                distanceList.append(distance)
    shortestDistance = min(distanceList)
    #print (distanceList)
    print (shortestDistance)

##shortest_dist([[45, -99], [24, 83], [-48, -68], [-97, 99],
##[-8, -77], [-2, 50], [44, 41], [-48, -58],
##[-1, 53], [14, 86], [31, 94], [12, -91],
##[33, 50], [82, 72], [83, -90], [10, 78],
##[7, -22], [90, -88], [-21, 5], [6, 23]])
##

def draw_grid(grid):
    turtle.setworldcoordinates(-1, -1, 10, 10)
    turtle.speed(0)
    turtle.delay(0)
    turtle.hideturtle()
    for i in range(len(grid)):
        coord2 = i
        row = grid[i]
        for n in range(len(row)):
            coord1 = n
            if row[n] != 1:
                turtle_square(coord1,coord2)
            

    
def turtle_square(coord1,coord2):
    x = coord1
    y = coord2
    turtle.penup()
    turtle.setpos(x,y)
    turtle.forward(0.5)
    turtle.right(90)
    turtle.forward(0.5)
    turtle.pendown()
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(1)
    turtle.right(90)
    turtle.forward(1)
    turtle.right(90)
    turtle.forward(1)
    turtle.right(90)
    turtle.forward(1)
    turtle.end_fill()

##draw_grid([[0,0,0,0,0,0,0,0,0,0],
##[0,0,0,0,0,0,0,0,0,0],
##[0,0,0,0,0,0,0,1,0,0],
##[0,0,0,0,0,0,1,1,0,0],
##[0,0,0,0,0,0,0,0,0,0],
##[0,0,0,0,0,0,0,0,0,0],
##[0,0,1,0,0,0,0,0,0,0],
##[0,0,1,0,0,0,0,0,0,0],
##[0,0,0,0,0,0,0,0,0,0],
##[0,0,0,0,0,0,0,0,0,0]])

##draw_grid([[0,0,0,0,0,0,0,0,0,0],
##[0,1,0,0,0,1,1,1,1,0],
##[0,1,0,1,1,1,0,0,1,0],
##[0,1,1,1,0,1,0,0,1,0],
##[0,1,0,1,0,1,1,0,0,0],
##[0,0,1,1,1,1,0,1,1,0],
##[0,0,1,0,0,1,1,1,0,0],
##[0,0,1,1,1,0,0,1,0,0],
##[0,0,1,0,1,0,1,1,1,0],
##[0,0,0,0,0,0,0,0,0,0]])


##def move_up():
##    turtle.showturtle()
##    turtle.setheading(90)
##    turtleX = round(turtle.xcor())
##    turtleY = round(turtle.ycor())
##    grid = grid1
##    if grid[turtleY+1][turtleX] == 1:
##        turtle.forward(1)
##
##
##def move_right():
##    turtle.showturtle()
##    turtle.setheading(0)
##    turtleX = round(turtle.xcor())
##    turtleY = round(turtle.ycor())
##    grid = grid1
##    if grid[turtleY][turtleX+1] == 1:
##        turtle.forward(1)
##
##def move_left():
##    turtle.showturtle()
##    turtle.setheading(180)
##    turtleX = round(turtle.xcor())
##    turtleY = round(turtle.ycor())
##    grid = grid1
##    if grid[turtleY][turtleX-1] == 1:
##        turtle.forward(1)
##
##def move_down():
##    turtle.showturtle()
##    turtle.setheading(270)
##    turtleX = round(turtle.xcor())
##    turtleY = round(turtle.ycor())
##    grid = grid1
##    if grid[turtleY-1][turtleX] == 1:
##        turtle.forward(1)

##draw_grid(grid1)
##
##turtle.color("blue")
##turtle.penup()
##turtle.setpos(1,1)
##turtle.pendown()
##turtle.speed(0)
##turtle.onkeypress(move_up, "Up")
##turtle.onkeypress(move_right, "Right")
##turtle.onkeypress(move_left, "Left")
##turtle.onkeypress(move_down, "Down")
##turtle.listen()
##turtle.mainloop()

def right_wall(grid):
    directionTurn = [90, 0, 270, 180]
    turtleState = True
    draw_grid(grid)
    turtle.penup()
    turtle.setpos(1,1)
    turtle.setheading(0)
    turtle.pendown()
    turtle.showturtle()
    turtle.color("blue")
    while turtleState == True:
        for i in range(4):
            turtle.right(directionTurn[i])
            turtle.forward(1)
            turtleX = round(turtle.xcor())
            turtleY = round(turtle.ycor())
            if (turtleX, turtleY) == (8, 8):
                turtleState = False
            if grid[turtleY][turtleX] == 0:
                turtle.undo()
                turtle.undo()
            if grid[turtleY][turtleX] == 1:
                break
            


        


##        turtleX = round(turtle.xcor())
##        turtleY = round(turtle.ycor())
##        turtle.right(90)
##        turtle.forward(1)
##        turtleX = round(turtle.xcor())
##        turtleY = round(turtle.ycor())
##        if (turtleX, turtleY) == (8, 8):
##            turtleState = False
##        if grid[turtleY][turtleX] == 0:
##            for i in range(2):
##                turtle.undo()
##            turtle.forward(1)
##            turtleX = round(turtle.xcor())
##            turtleY = round(turtle.ycor())
##            if (turtleX, turtleY) == (8, 8):
##                turtleState = False
##            if grid[turtleY][turtleX] == 0:
##                turtle.undo()
##                turtle.left(90)
##                turtle.forward(1)
##                turtleX = round(turtle.xcor())
##                turtleY = round(turtle.ycor())
##                if (turtleX, turtleY) == (8, 8):
##                    turtleState = False
##                if grid[turtleY][turtleX] == 0:
##                    for i in range(2):
##                        turtle.undo()
##                    turtle.right(180)
##                    turtle.forward(1)
##                    turtleX = round(turtle.xcor())
##                    turtleY = round(turtle.ycor())
##                    if (turtleX, turtleY) == (8, 8):
##                        turtleState = False
            
            
            
        
        
    

    
##right_wall([[0,0,0,0,0,0,0,0,0,0],
##[0,1,1,1,1,0,1,1,1,0],
##[0,1,0,0,0,0,1,0,1,0],
##[0,1,1,1,1,1,1,1,1,0],
##[0,1,0,0,0,0,1,0,0,0],
##[0,1,1,1,1,1,1,1,1,0],
##[0,0,1,0,0,0,1,0,1,0],
##[0,0,1,0,0,0,0,0,0,0],
##[0,1,1,1,1,1,1,1,1,0],
##[0,0,0,0,0,0,0,0,0,0]])

right_wall([[0,0,0,0,0,0,0,0,0,0],
[0,1,0,0,0,1,1,1,1,0],
[0,1,0,1,1,1,0,0,1,0],
[0,1,1,1,0,1,0,0,1,0],
[0,1,0,1,0,1,1,0,0,0],
[0,0,1,1,1,1,0,1,1,0],
[0,0,1,0,0,1,1,1,0,0],
[0,0,1,1,1,0,0,1,0,0],
[0,0,1,0,1,0,1,1,1,0],
[0,0,0,0,0,0,0,0,0,0]])
         

