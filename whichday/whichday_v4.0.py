"""
    作者：郑智慧
    版本：4.0
    日期：2019/7/13
    功能：输入日期判断第几天-元组tuple使用
    2.0功能：用列表list实现
    3.0功能：用集合set实现
    4.0功能：用字典dict实现
"""
import datetime as dt


def is_leap_year(year):
    """
    输入年份判断是否是闰年
    :param year: 年份
    :return: 是或否
    """
    is_leap = False
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        is_leap = True
    return is_leap


def main():
    """
    主函数
    :return:
    """
    input_date_str = input('请输入日期(yyyy/mm/dd): ')
    input_date = dt.datetime.strptime(input_date_str, format('%Y/%m/%d'))
    print(input_date)
    year = input_date.year
    month = input_date.month
    day = input_date.day

    month_day_dict = {1: 31,
                      2: 28,
                      3: 31,
                      4: 30,
                      5: 31,
                      6: 30,
                      7: 31,
                      8: 31,
                      9: 30,
                      10: 31,
                      11: 30,
                      12: 31}

    days = 0
    days += day
    for i in range(1, month):
        days += month_day_dict[i]
    if month > 2 and is_leap_year(year):
        days += 1

    print('这是{}年的第{}天。'.format(year, days))


if __name__ == "__main__":
    main()
