"""
    作者：郑智慧
    功能：BMR计算
    版本：6.0
    日期：2019/7/10
    4.0新增功能：判断用户在一行中输入的信息是否有误
    5.0新增功能：使用try-except
    6.0新增功能：将bmr计算封装到函数
"""


def bmrCal(input_list):
    """
        计算bmr
    """
    try:
        # 性别
        gender = input_list[0]
        # print(type(gender))

        # 体重(kg)
        weight = float(input_list[1])
        # print(type(weight))

        # 身高(cm)
        height = float(input_list[2])
        # print(type(height))

        # 年龄
        age = int(input_list[3])
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
            print("你的性别{}, 体重{}, 身高{}, 年龄{}".format(gender, weight, height, age))
            print("基础代谢率", bmr, "大卡")
        else:
            print("不支持的性别")
    except ValueError:
        print("请输入正确信息")
    except IndexError:
        print("您输入的信息过少")
    except:
        print("程序异常，已自行退出")


def main():
    """
        主函数
    """
    y_or_n = input("是否退出程序(y/n):")
    while y_or_n != 'y':
        print("请输入以下信息，用空格分隔")
        input_str = input("性别 体重(kg) 身高(cm) 年龄: ")
        input_list = input_str.split(" ")
        print(input_list)
        bmrCal(input_list)

        print("**************************************************")
        y_or_n = input("是否退出程序(y/n):")

if __name__ == "__main__":
    main()