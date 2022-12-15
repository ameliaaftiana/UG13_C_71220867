import turtle

s=turtle.Screen()
t=turtle.Turtle()
s.bgcolor('purple')

t.shape('turtle')

t.pencolor('white')
t.pensize('20')
t.speed(0.6)


#A
t.forward(90)
t.right(244)
t.forward(100)
t.left(127)
t.forward(180)
t.penup()
t.goto(76,30)
t.left(50)
t.pendown()
t.forward(107)

#6
t.penup()
t.goto(180,-67)
t.left(157)
t.pendown()
t.forward(153)
t.right(90)
t.forward(70)
t.penup()
t.goto(180,-67)
t.pendown()
t.forward(90)
t.left(90)
t.forward(70)
t.left(90)
t.forward(90)

#p
t.penup()
t.goto(343,-68)
t.right(90)
t.pendown()
t.forward(153)
t.right(90)
t.forward(75)
t.right(45)
t.forward(20)
t.right(45)
t.forward(50)
t.right(45)
t.forward(25)
t.right(45)
t.forward(62)

#8
t.penup()
t.goto(230,230)
t.pendown()
t.circle(45,360)
t.penup()
t.goto(230,318)
t.pendown()
t.circle(45,360)

#7
t.penup()
t.goto(180,-123)
t.pendown()
t.right(180)
t.forward(90)
t.right(110)
t.forward(155)



s.exitonclick()
