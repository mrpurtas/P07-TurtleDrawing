# import turtle
# turtle_screen = turtle.Screen()
# turtle_screen.bgcolor("#40E0D0")
# turtle_screen.title("Python Turtle")

# turtle.speed(0)

# turtle_instance = turtle.Turtle()
# turtle_instance.color("blue")


# turtle_colors = ["red","purple", "blue", "green", "orange","yellow"]

# for i in range(15):
#     turtle_instance.color(turtle_colors[i % 6])
#     turtle_instance.circle(10 * i)
#     turtle_instance.circle(-10 * i )
#     turtle_instance.left(i)



# turtle.mainloop()
# #turtle.done()


import turtle

colors_turtle = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
turtle_instance = turtle.Turtle()
#t = turtle.Pen()
turtle.bgcolor('black')

for i in range(360):
    turtle_instance.pencolor(colors_turtle[i % 6])
    turtle_instance.width(i // 100 + 1)
    turtle_instance.forward(i)
    turtle_instance.left(60)

#turtle.done()
turtle.mainloop()