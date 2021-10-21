import turtle, platform, math

#TODO: Fill out the Purpose, Input Parameter(s), and Return Value
# for each of the two functions below in comments, and then write
# additional functions for parts B and C, and fill out the same information
# for those functions as well.

#Remember, you must place a # before any comment, or it will be
# interpreted as Python code, and will probably cause errors.

# cents
#==========================================
# Purpose:
#   
# Input Parameter(s):
#   
# Return Value:
#   
#==========================================

def cents(quarters, dimes, nickels, pennies):
    total = 0
    total += quarters*25
    total += dimes*10
    total += nickels*5
    total += pennies
    return total

# draw_M
#==========================================
# Purpose:
#   
# Input Parameter(s):
#   
# Return Value:
#   
#==========================================

def draw_M():
    turtle.delay(0)
    turtle.bgcolor("gold")
    turtle.hideturtle()
    turtle.color("maroon")
    turtle.penup()
    turtle.setpos(-200,-100)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(80)
    turtle.right(120)
    turtle.forward(28)
    turtle.right(120)
    turtle.forward(14)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(128)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(14)
    turtle.right(120)
    turtle.forward(28)
    turtle.right(120)
    turtle.forward(80)
    turtle.right(120)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(28)
    turtle.right(60)
    turtle.forward(140)
    turtle.right(120)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(52)
    turtle.right(120)
    turtle.forward(52)
    turtle.right(120)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(140)
    turtle.right(60)
    turtle.forward(28)
    turtle.left(90)
    turtle.forward(64)
    turtle.end_fill()

# Part B: star8
#==========================================
# Purpose:
#   
# Input Parameter(s):
#   
# Return Value:
#   
#==========================================

def star8():
    for i in range(8):
        turtle.forward(200)
        turtle.left(135)
    return

star8()

# Part C: trajectory
#==========================================
# Purpose:
#   
# Input Parameter(s):
#   
# Return Value:
#   
#==========================================

def trajectory(height, speed, angle):
    radAngle = angle* (math.pi/180)
    horizontalSpeed = speed * math.cos(radAngle)
    verticalSpeed = speed * math.sin(radAngle)
    flightTime = (verticalSpeed + math.sqrt((verticalSpeed**2 + 19.6*height)))/9.8
    flightDistance = horizontalSpeed * flightTime
    
    print ("Horizontal Speed: " + str(round(horizontalSpeed,3)) + " m/s")
    print ("Vertical Speed: " + str(round(verticalSpeed,3)) + " m/s")
    print ("Flight Time: " + str(round(flightTime,3)) + " s")
    return round(flightDistance,3)


