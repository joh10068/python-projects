import turtle
import random

def div27(num):
    for i in range(2,8):
        if num % i == 0:
            divisible = True
            break
        else:
            divisible = False
    return divisible

def spiro(num, length):
    rotation = 360/num
    for i in range(num):
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(length)
            turtle.left(90)
            r = random.random()
            g = random.random()
            b = random.random()
            turtle.color(r,g,b)
        turtle.end_fill()
        turtle.left(rotation)

def mul(a,b):
    product = 0
    for i in range(b):
        product += a
    return product
        
def mulW(a,b):
    product = 0
    i = 0
    while i < b:
        product += a
        i += 1
    return product

def expo(x,y):
    prod = 1
    for i in range(y):
        total = 0
        value = mul(x,prod)
        prod = total
    return prod
