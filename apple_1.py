#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("background.gif")
wn.addshape(apple_image) # Make the screen aware of the new file
apple = trtl.Turtle()
letter_drawer = trtl.Turtle()
letter_drawer.hideturtle()
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  letter_a()
  wn.update()
def apple_fall():
  letter_drawer.clear()
  apple.penup()
  apple.goto(apple.xcor(), -165)
  apple.clear()
  apple.hideturtle()
  apple.pendown()
def letter_a():
    letter_drawer.penup()
    letter_drawer.goto(apple.xcor()-20, apple.ycor()-45)
    letter_drawer.color("white")
    letter_drawer.write("A", font=("Arial", 40, "bold"))

#-----function calls-----
draw_apple(apple)
wn.onkeypress(apple_fall,"a")
wn.listen()
wn.mainloop()
