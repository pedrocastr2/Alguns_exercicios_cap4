import turtle
t = turtle.Pen()
t.penup()
turtle.bgcolor("black")
#pede o número de lados ao usuário , tendo como padrão igual igual 4 ,minimo igual 2 e máximo igual a 6 
sides = int(turtle.numinput("Number of sides ","How many sides in your spiral of spirals? (2-6) ",4,2,6))
colors = ["red","yellow","blue","green","purple","orange"]
#nosso laço ecterno para a espiral
for m in range(100):
    t.forward(m*4)
    position  = t.position() #armazena esse canto da espirral
    heading = t.heading() #armazema a direção para qual estamos seguindo
    print(position,heading)
    #nosso laço interno de espirais
    #desenha uma pequena espiral em cada canto da espiral maior
    for n in range(int(m / 2)):
     t.pendown()
     t.pencolor(colors[n%sides])
     t.forward(2 * n)
     t.right(360 / sides - 2)
     t.penup()
        
    t.setx(position[0]) #retorna a posição x da espiral maior
    t.sety(position[1])  #retorna a posição y da espiral maior
    t.setheading(heading) #Aponte na diração que estavamos na espiral maior
    t.left(360/sides +2) #Aponte para o próximo que estavamos na espiral maior
