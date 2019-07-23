"""
    作者：郑智慧
    版本：2.0
    日期：2019/07/14
    功能：生活小工具
    2.0功能：用类来实现；数据保存到文件中
"""
import time as tm


class FileTool():
    """
        文件操作类
    """
    def __init__(self, filepath):
        self.filepath = filepath

    def write_to_file(self, content):
        with open(self.filepath, 'a') as f:
            f.write(content)

    def read_from_file(self):
        with open(self.filepath, 'r') as f:
            content = f.readlines()
        return content


class LifeTool():
    """
        生活小工具的类
    """
    def __init__(self):
        pass

    def bmrCal(self, input_list):
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
                print("你的性别是{}, 体重{}, 身高{}, 年龄{}".format(gender, weight, height, age))
                print("基础代谢率", bmr, "大卡")
            else:
                print("不支持的性别")
        except ValueError:
            print("请输入正确信息")
        except IndexError:
            print("您输入的信息过少")
        except:
            print("程序异常，已自行退出")
        return bmr

    def process_bmr(self):
        """
            获取用户参数，计算bmr并输出
        """
        print("请输入以下信息，用空格分隔")
        input_str = input("性别 体重(kg) 身高(cm) 年龄: ")
        input_list = input_str.split(" ")
        # print(input_list)
        return self.bmrCal(input_list)

    def process_currency_converter(self):
        """
            获取用户输入金额，根据汇率转换后输出
        """
        # 汇率
        USD_VS_RMB = 6.77
        out_money = 0

        # 带单位的货币的输入
        currency_str_value = input('请输入带单位的货币金额(CNY/USD)：')

        # 获取货币单位
        unit = currency_str_value[-3:]

        if unit in ['CNY']:
            exchange_rate = 1 / USD_VS_RMB
        elif unit in ['USD']:
            exchange_rate = USD_VS_RMB
        else:
            exchange_rate = -1

        if exchange_rate != -1:
            in_money = eval(currency_str_value[:-3])

            # 使用lambda定义函数
            convert_currency2 = lambda x: x * exchange_rate
            out_money = convert_currency2(in_money)
            # out_money = convert_currency(in_money, exchange_rate)
            if 'CNY' == unit:
                print('转换后的金额为:{:.2f}USD'.format(out_money))
            elif 'USD' == unit:
                print('转换后的金额为:{:.2f}CNY'.format(out_money))
        else:
            print('不支持该货币')
        return out_money

    def process_temp_converter(self):
        """
            获取用户输入温度值，转换后输出
        """
        out_temp = 0
        TempStr = input('请输入带有符号的温度值(C/F)：')
        if TempStr[-1] in ['F', 'f']:
            out_temp = (eval(TempStr[0:-1]) - 32) / 1.8
            print('转换后的温度是{: .2f}C'.format(out_temp))
        elif TempStr[-1] in ['C', 'c']:
            out_temp = 1.8 * eval(TempStr[0:-1]) + 32
            print('转换后的温度是{: .2f}F'.format(out_temp))
        else:
            print('输入格式错误')
        return out_temp


def main():
    """
        主函数
    """
    mylifetool = LifeTool()
    mypath = "life_tool.txt"
    myfiletool = FileTool(mypath)

    tool_num = input("请输入你要使用的工具编号(1-BMR计算 2-汇率转换 3-温度转换 4-退出程序)(回车结束)：")
    now_time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
    myfiletool.write_to_file("{}\n用户输入工具编号{}\n".format(now_time, tool_num))
    while '4' != tool_num:
        if '1' == tool_num:
            bmr = mylifetool.process_bmr()
            myfiletool.write_to_file("计算的BMR是:{:.0f}\n".format(bmr))
        elif '2' == tool_num:
            out_money = mylifetool.process_currency_converter()
            myfiletool.write_to_file("转换后的金额是:{:.2f}\n".format(out_money))
        elif '3' == tool_num:
            out_temp = mylifetool.process_temp_converter()
            myfiletool.write_to_file("转换后的温度是:{:.2f}\n".format(out_temp))
        else:
            print("输入非法")
            myfiletool.write_to_file("输入非法\n")
        print("*************************************")
        tool_num = input("请输入你要使用的工具编号(1-BMR计算 2-汇率转换 3-温度转换 4-退出程序)(回车结束)：")
        myfiletool.write_to_file("{}\n用户输入工具编号{}\n".format(now_time, tool_num))
    print("程序已退出！")
    myfiletool.write_to_file("程序退出\n\n")


if __name__ == "__main__":
    main()
