"""
    作者：郑智慧
    功能：52周存钱
    版本：5.0
    日期：2019/7/12
    2.0新增功能：记录每周存钱数
    3.0新增功能：使用for遍历
    4.0新增功能：函数参数传递
    5.0新增功能：用户输入日期，显示该日期存款金额
"""
import math
import datetime


def money_saving_in_n_weeks(money_per_week, increase_money, total_week):
    money_list = []
    saved_money_list = []
    for i in range(total_week):
        # 计算每周存钱数
        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        saved_money_list.append(saving)
        print("第{}周，存入{}元，总金额{}元".format(i + 1, money_per_week, saving))

        # 更新下一周存钱金额
        money_per_week += increase_money
    return saved_money_list


def main():
    """
        主函数
    """
    money_per_week = float(input("请输入首周存钱数: "))
    increase_money = float(input("请输入每周递增的钱数: "))
    total_week = int(input("请输入存钱周数: "))
    saved_money_list = money_saving_in_n_weeks(money_per_week, increase_money, total_week)
    date_input_str = input('请输入日期(yyyy/mm/dd)')
    date_input = datetime.datetime.strptime(date_input_str, format('%Y/%m/%d'))
    week_num = date_input.isocalendar()[1]
    print('第{}周的存款金额是:{}元'.format(week_num, saved_money_list[week_num - 1]))


if __name__ == "__main__":
    main()
