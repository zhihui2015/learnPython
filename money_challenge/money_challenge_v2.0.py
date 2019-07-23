"""
    作者：郑智慧
    功能：52周存钱
    版本：2.0
    日期：2019/7/10
    2.0新增功能：记录每周存钱数
"""
import math


def main():
    """
        主函数
    """
    i = 1
    saving = 0
    money_per_week = 10
    increase_money = 10
    total_week = 52
    money_list = []

    while i <= total_week:
        # 计算每周存钱数
        money_list.append(money_per_week)
        saving = math.fsum(money_list)

        print("第{}周，存入{}元，总金额{}元".format(i, money_per_week, saving))

        # 更新下一周存钱金额
        money_per_week += increase_money
        i += 1


if __name__ == "__main__":
    main()
