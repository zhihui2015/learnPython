"""
    作者：郑智慧
    版本：0.4
    日期：2019/07/15
    功能：模拟摇骰子-list+random
    0.2功能：模拟两个骰子-dict+random
    0.3功能：投掷骰子数据可视化-matplotlib
    0.4功能：对结果进行数据统计和分析-直方图
"""
import random as rd
import matplotlib.pyplot as plt

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


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
    total_times = 10000

    # 记录骰子结果
    roll_list = []

    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()
        roll_list.append(roll1+roll2)

    # 绘制直方图
    plt.hist(roll_list, bins=range(2, 14), normed=1, edgecolor='black', linewidth=1)
    plt.title("骰子点数统计")
    plt.xlabel("点数")
    plt.ylabel("频率")
    plt.ylabel("频率")
    plt.show()


if __name__ == "__main__":
    main()


