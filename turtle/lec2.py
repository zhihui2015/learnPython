"""
    画树
"""

import turtle as tt



def drawBranch(root_len, root_width):
    """
        画树的分支
    """
    if root_len <= 15:
        tt.pencolor("green")
    else:
        tt.pencolor("brown")
    if root_len > 5:
        if root_width < 2:
            root_width = 2
        tt.pensize(root_width)
        tt.forward(root_len)
        print("向前", root_len)
        tt.right(20)
        print("向右20")
        drawBranch(root_len - 10, root_width - 3)

        tt.left(40)
        print("向左40")
        drawBranch(root_len - 10, root_width - 3)

        tt.right(20)
        print("向右20")
        tt.backward(root_len)
        tt.pencolor("brown")
        print("向后", root_len)




tt.penup()
tt.pensize(2)
tt.pencolor("brown")
tt.seth(90)
tt.backward(300)
tt.pendown()

root_len = 100
root_width = 20

drawBranch(root_len, root_width)

tt.exitonclick()
