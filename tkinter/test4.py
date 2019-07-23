import turtle as t

t.setup(650, 350, 300, 300)
t.penup()
t.fd(-250)
t.pensize(10)
t.pencolor("black")
t.pendown()
t.seth(0)
t.fd(100)
for i in range(8):
    t.left(80)
    t.fd(100)
t.done()
