#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("background.gif")
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
  apple.color("white")
  apple.write("A", font=("Arial", 40, "bold")) 
def apple_fall():
  apple.penup()
  apple.goto(apple.xcor(), -165)
  apple.pendown()

#-----function calls-----
draw_apple(apple)
wn.onkeypress(apple_fall,"a")
wn.listen()
wn.mainloop()