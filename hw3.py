
state = 1

def choice(text,optionA,optionB,optionC):

    print(text)
    print("A: " + optionA)
    print("B: " + optionB)
    print("C: " + optionC)
    print("Choose A, B, or C:")

    choice = str(input())

    if choice == 'A' or choice == 'B' or choice == 'C':
        return(choice)
    else:
        print("Invalid option, defaulting to A")
        choice = 'A'
              
    return(choice)




def adventure():
    global state
    ending = None
    nested_choice = ""

    if state == 1:
        nested_choice = choice("You are at a door","Open door","Touch knob","RUN!")
        if nested_choice == 'A':
            state = 2
            adventure()
        if nested_choice == 'B':
            ending = False
            print("you lost")
            return(ending)
        if nested_choice == 'C':
            state = 3
            adventure()

    if state == 2:
        nested_choice = choice("You are at a hole","Jump down","Look down","RUN!")
        if nested_choice == 'A':
            ending = False
            #state = 5
            print("you win")
        if nested_choice == 'B':
            state = 4
            adventure()
        if nested_choice == 'C':
            state = 3
            adventure()

    if state == 3:
        nested_choice = choice("You are at a glory hole","Stick in","Put mouth","RUN!")
        if nested_choice == 'A':
            ending = False
            print("you lose")
        if nested_choice == 'B':
            state = 4
            adventure()
        if nested_choice == 'C':
            ending = True
            print("you win")

    if state == 4:
        nested_choice = choice("You are about to die","Accept death","Pull down pants","RUN!")
        if nested_choice == 'A':
            ending = True
            print("you win")
        if nested_choice == 'B':
            ending = True
            print("you win")
        if nested_choice == 'C':
            ending = False
            print("you lose")


                 
        
    
