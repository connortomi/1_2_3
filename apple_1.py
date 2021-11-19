#   a123_apple_1.py
#import modules
import turtle as trtl
import random as rand
#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("background.gif")
wn.addshape(apple_image) # Make the screen aware of the new file
#create turtles
apple1 = trtl.Turtle()
apple2 = trtl.Turtle()
apple3 = trtl.Turtle()
apple4 = trtl.Turtle()
apple5 = trtl.Turtle()
letter_drawer1 = trtl.Turtle()
#assign variables and create letter list
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
random_letter = rand.randint(0,len(letters)-1)
x = letters[random_letter]
#-----functions-----
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  random_letter()
  wn.update()
def apple_fall():
  letter_drawer1.clear()
  apple1.penup()
  apple1.goto(apple1.xcor(), -165)
  apple1.clear()
  apple1.hideturtle()
  apple1.pendown()
#find a random letter from the list and draw it
def random_letter():
    letter_drawer1.penup()
    letter_drawer1.goto(apple1.xcor()-20, apple1.ycor()-45)
    letter_drawer1.color("white")
    letter_drawer1.write(x, font=("Arial", 40, "bold"))
#call the functions
draw_apple(apple1)
wn.onkeypress(apple_fall, x.lower())
wn.listen()
wn.mainloop()
