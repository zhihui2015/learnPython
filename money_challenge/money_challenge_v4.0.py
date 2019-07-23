"""
    作者：郑智慧
    功能：52周存钱
    版本：4.0
    日期：2019/7/10
    2.0新增功能：记录每周存钱数
    3.0新增功能：使用for遍历
    4.0新增功能：函数参数传递
"""
import math


def money_saving_in_n_weeks(money_per_week, increase_money, total_week):
    money_list = []
    for i in range(total_week):
        # 计算每周存钱数
        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        print("第{}周，存入{}元，总金额{}元".format(i + 1, money_per_week, saving))

        # 更新下一周存钱金额
        money_per_week += increase_money
    return saving


def main():
    """
        主函数
    """
    money_per_week = float(input("请输入首周存钱数: "))
    increase_money = float(input("请输入每周递增的钱数: "))
    total_week = int(input("请输入存钱周数: "))
    saving = money_saving_in_n_weeks(money_per_week, increase_money, total_week)
    print("主函数的saving = ", saving)


if __name__ == "__main__":
    main()
