"""
    绘制五角星
"""

import turtle as tt


def dramFiveStar(size):
    count = 1
    while count <= 5:
        tt.forward(size)
        tt.right(144)
        count = count + 1
    size += 10
    if size <= 100:
        dramFiveStar(size)





def main():
    """
        主函数
    """
    tt.penup()
    tt.pensize(2)
    tt.pencolor("red")
    tt.pendown()

    size = 50
    dramFiveStar(size)
    # while size <= 100:
    #     dramFiveStar(size)
    #     size = size + 10

    tt.exitonclick()





if __name__ == '__main__':
    main()

