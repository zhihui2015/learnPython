"""
    作者：郑智慧
    版本：5.0
    日期：2019/7/13
    功能：输入日期判断第几天-元组tuple使用
    2.0功能：用列表list实现
    3.0功能：用集合set实现
    4.0功能：用字典dict实现
    5.0功能：用dict+set实现
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

    day_month_dict = {30: {4, 6, 9, 11},
                      31: {1, 3, 5, 7, 8, 10, 12}}
    days = 0
    days += day
    for i in range(1, month):
        if i in day_month_dict[30]:
            days += 30
        elif i in day_month_dict[31]:
            days += 31
        else:
            days += 28
    if month > 2 and is_leap_year(year):
        days += 1

    print('这是{}年的第{}天。'.format(year, days))


if __name__ == "__main__":
    main()
