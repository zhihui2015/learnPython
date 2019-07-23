"""
    作者：郑智慧
    版本：0.3
    日期：2019/07/15
    功能：模拟摇骰子-list+random
    0.2功能：模拟两个骰子-dict+random
    0.3功能：投掷骰子数据可视化-matplotlib
"""
import random as rd
import matplotlib.pyplot as plt


def roll_dice():
    """
        模拟摇骰子
    """
    roll = rd.randint(1, 6)
    return roll


def main():
    """
        主函数
    """
    total_times = 1000
    # 创建一个列表包含11个元素
    result_list = [0] * 11
    # 创建一个列表包含从2到12的元素
    roll_list = list(range(2, 13))
    # 使用zip将上述两个列表连接成元组，再用dict将元组转化为字典
    roll_dict = dict(zip(roll_list, result_list))

    # 每次骰子的值
    roll1_list = []
    roll2_list = []

    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()
        roll1_list.append(roll1)
        roll2_list.append(roll2)
        for j in range(2, 13):
            if (roll1+roll2) == j:
                roll_dict[j] += 1

    for i, result in roll_dict.items():
        print("点数{}的次数:{},频率:{}".format(i, result, result/total_times))

    # 绘制坐标图
    x = range(1, total_times+1)
    plt.scatter(x, roll1_list, c='red', alpha=0.5)
    plt.scatter(x, roll2_list, c='green', alpha=0.5)
    plt.show()


if __name__ == "__main__":
    main()


