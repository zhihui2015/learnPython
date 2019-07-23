import turtle as t

t.setup(800, 400)
t.penup()
t.pensize(6)
t.pencolor("black")
t.seth(0)
t.pendown()
for i in range (4):
    t.left(45)
    t.fd(150)
    t.left(90)
    t.circle(150, 45)
    t.left(90)
    t.fd(150)
t.done()
