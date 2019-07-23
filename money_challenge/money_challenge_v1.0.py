"""
    作者：郑智慧
    功能：52周存钱
    版本：1.0
    日期：2019/7/10
"""


def main():
    """
        主函数
    """
    i = 1
    saving = 0
    money_per_week = 10
    increase_money = 10
    total_week = 52

    while i <= total_week:
        # 计算每周存钱数
        saving += money_per_week
        print("第{}周，存入{}元，总金额{}元".format(i, money_per_week, saving))

        # 更新下一周存钱金额
        money_per_week += increase_money
        i += 1


if __name__ == "__main__":
    main()
