"""
    作者：郑智慧
    版本：2.0
    日期：2019/7/13
    功能：输入日期判断第几天-元组tuple使用
    2.0功能：用列表list实现
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

    days_per_month_in_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    print(days_per_month_in_list[:month-1])

    if is_leap_year(year):
        days_per_month_in_list[1] += 1
    days = sum(days_per_month_in_list[:month-1]) + day
    print('这是{}年的第{}天。'.format(year, days))


if __name__ == "__main__":
    main()
