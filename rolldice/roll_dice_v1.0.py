"""
    作者：郑智慧
    版本：0.1
    日期：2019/07/15
    0.1功能：模拟摇骰子
"""
import random as rd


def roll_dice():
    """
        模拟摇骰子
    """
    # 产生1到6的随机整数
    roll = rd.randint(1, 6)
    return roll


def main():
    """
        主函数
    """
    total_times = 100000
    # 初始化列表包含6个元素
    result_list = [0] * 6
    for i in range(total_times):
        roll = roll_dice()
        for j in range(1, 7):
            if roll == j:
                result_list[j-1] += 1

    for i, result in enumerate(result_list):
        print("点数{}的次数:{},频率:{}".format(i+1, result, result/total_times))


if __name__ == "__main__":
    main()


