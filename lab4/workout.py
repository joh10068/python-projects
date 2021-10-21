import turtle
import random

random.randint(1,4)


def jay_walk():
    i = 0
    while True:
        i += 1     
        random_var = random.randint(1,4)
        random_heading = (1 - random_var)*90
        turtle.setheading(random_heading)
        turtle.forward(30)
        random_xcor = turtle.xcor()
        print(random_xcor)
        random_ycor = turtle.ycor()
        random_blocks = i
        if random_xcor > 300 or random_xcor < -300:
            turtle.write(random_blocks, font=("Arial", 20, "normal"))
            break
        if random_ycor > 300 or random_ycor < -300:
            turtle.write(random_blocks, font=("Arial", 20, "normal"))
            break
        
            
        
        
    
def monte_pi():
    red_dots = 0
    green_dots = 0
    turtle.speed(0)
    turtle.delay(0)
    for i in range(1000):
        random_xcor = 150*random.uniform(-1,1)
        random_ycor = 150*random.uniform(-1,1)
        turtle.penup()
        turtle.setx(random_xcor)
        turtle.sety(random_ycor)
        if turtle.distance(0,0) > 150:
            turtle.pendown()
            turtle.dot(10, "red")
            red_dots += 1
        if turtle.distance(0,0) <= 150:
            turtle.pendown()
            turtle.dot(10, "green")
            green_dots += 1
    pi_ratio = green_dots/red_dots
    print(pi_ratio)

            


monte_pi()
        
        
    
