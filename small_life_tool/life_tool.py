"""
    作者：郑智慧
    版本：1.0
    日期：2019/07/14
    功能：生活小工具
"""
from bmr_cal import process_bmr
from currency_converter import process_currency_converter
from temp_convert import process_temp_converter


def main():
    """
        主函数
    """
    tool_num = input("请输入你要使用的工具编号(1-BMR计算 2-汇率转换 3-温度转换 4-退出程序)(回车结束)：")
    while '4' != tool_num:
        if '1' == tool_num:
            process_bmr()
        elif '2' == tool_num:
            process_currency_converter()
        elif '3' == tool_num:
            process_temp_converter()
        else:
            print("输入非法")
        print("*************************************")
        tool_num = input("请输入你要使用的工具编号(1-BMR计算 2-汇率转换 3-温度转换 4-退出程序)(回车结束)：")
    print("程序已退出！")


if __name__ == "__main__":
    main()

