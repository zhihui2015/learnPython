import turtle as t

t.setup(650, 350, 300, 300)
t.penup()
t.pensize(2)
t.pencolor("black")
t.pendown()
t.seth(0)
t.fd(50)
for i in range(5):
    t.left(60)
    t.fd(50)
t.done()
