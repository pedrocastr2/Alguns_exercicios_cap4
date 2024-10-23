import turtle
t = turtle.Pen()
turtle.bgcolor("black")

colors = ["red","yellow","blue","green","orange","purple","white"]

number_of_circles = int(turtle.numinput("Numero de circulos","Qual número circles de sua rossete",6))

for x in range(number_of_circles):
    t.pencolor(colors[x % len(colors)])
    t.circle(100)
    t.left(360/number_of_circles)
    