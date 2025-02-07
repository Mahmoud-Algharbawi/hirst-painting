
import colorgram
import turtle as t
import random

# setup the screen and initialize the turtle objects
screen = t.Screen()
my_turtle = t.Turtle()

screen.colormode(255)
screen.bgcolor("black")
my_turtle.speed("fastest")
my_turtle.color("white")
my_turtle.hideturtle()

#set the dot size to 20
my_turtle.pensize(20)

"""
Function to extract the colors from the image provided in main

Params: 
      image file -> file
      number of colors to extract -> int
Return:
      rgb_list -> list
          a list of tuples of (r, g, b) values

"""  

def extract_colors(image, number_of_colors):
    colors = colorgram.extract(image, number_of_colors)
    rgb_list = []
    for color in colors:
        rgb_list.append((color.rgb.r, color.rgb.g, color.rgb.b))
        
    print(rgb_list)
    return rgb_list




# A function to draw the dots on the canvas
def draw_dots(dots, color_list):
    
    # go to the bottom left corner first
    my_turtle.penup()
    my_turtle.seth(225)
    my_turtle.forward(30 * dots)
       

    
    for i in range(dots):
        my_turtle.seth(0)
        
        for j in range(dots):
            my_turtle.dot(20, random.choice(color_list))
            my_turtle.forward(50)
    
        return_to_line_start(dots)

 
            

def return_to_line_start(dots):
    my_turtle.seth(90)
    my_turtle.forward(50)
    my_turtle.seth(180)
    my_turtle.forward(50 * dots)
    my_turtle.seth(0)



if __name__ == '__main__':
    
    # Extract the colors from the drawing proved
    # Parameters: (drawing file name, number of colors)
    colors = extract_colors('drawing.jpg', 30)
    draw_dots(15, colors)
    

    
    screen.exitonclick()