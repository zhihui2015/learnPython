"""
    输出星期的简写
"""


week_all_str = "MonTueWedThuFriSatSun"

week_str = input("请输入星期几(1-7)(按Q退出程序):")

while week_str != 'Q':
    week_n = int(week_str)
    if week_n <= 7:
        pos = (int(week_n) - 1) * 3
        print("星期的简写是:", week_all_str[pos:pos+3])
    else:
        print("输入的数字无效")
    week_str = input("请输入星期几(1-7)(按Q退出程序):")
print("程序已退出")
