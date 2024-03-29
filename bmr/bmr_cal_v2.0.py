"""
    作者：郑智慧
    功能：BMR计算
    版本：2.0
    日期：2019/7/9
    新增功能：增加用户输入
"""

def main():
    """
        主函数
    """
    y_or_n = input("是否退出程序(y/n):")
    while y_or_n != 'y':
        # 性别
        gender = input('性别:')
        # print(type(gender))

        # 体重(kg)
        weight = float(input('体重(kg):'))
        # print(type(weight))

        # 身高(cm)
        height = float(input('身高(cm):'))
        # print(type(height))

        # 年龄
        age = int(input('年龄:'))
        # print(type(age))

        if gender == '男':
            # 男性
            bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
        elif gender == '女':
            # 女性
            bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
        else:
            bmr = -1

        if bmr != -1:
            print("基础代谢率{}大卡".format(bmr))
        else:
            print("不支持的性别")

        print("**************************************************")
        y_or_n = input("是否退出程序(y/n):")

if __name__ == "__main__":
    main()