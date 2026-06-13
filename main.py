import turtle
import pandas as p
sc = turtle.Screen()
sc.title("US STATE QUIZ")
img = "img.gif"
t = turtle.Turtle()
# SETTING UP THE BACKGROUND IMAGE  
sc.addshape(img)
t.shape(img)

# READS DATA FROM CSV FILE 
data=p.read_csv("50_states.csv")

# CONVERTS THE STATES DATA INTO LIST 
states=list(data['state'])

# KEEPS TRACK OF THE CORRECT GUESSED STATES 
correct=[]

# CORE LOGIC 
while len(correct)<50:
    if len(correct)==0:
        user_input=sc.textinput("Guess The State Game ", "Enter Any State Name :",)
    else:
        user_input=sc.textinput(f"{len(correct)}/50 Are Correct ", "Enter another State Name :",)
    user_input=user_input.title()
    # FORCED EXIT 
    if user_input=='Exit':
        # SAVES THE STATES YOU MISSED INTO A CSV FILE 
        not_guessed=[]
        for i in states:
            if i not in correct:
                not_guessed.append(i)
        new_df=p.DataFrame(not_guessed)
        new_df.to_csv("States_you_missed.csv")
        break
    if user_input in states and user_input not in correct :
        correct.append(user_input)
        xc=data[data['state']== user_input].x.item()
        yc=data[data['state']== user_input].y.item()
        a=turtle.Turtle()
        a.hideturtle()
        a.speed(1)
        a.penup()
        a.goto(xc,yc)
        a.write(user_input)
    else:
        user_input=sc.textinput(f"{len(correct)}/50 Are Correct ", "Enter another State Name :",)

# MAKES THE TURTLE WINDOW STAY 
turtle.mainloop()
turtle.done()

# FOR GETTING THE CORDINATES OF MOUSE CLICKS 
# def getcor(x,y):
#     print(f"x:{x},y:{y}")

# turtle.onscreenclick(getcor)

# sc.exitonclick()