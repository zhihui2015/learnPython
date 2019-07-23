"""
    作者：郑智慧
    功能：凯撒密码
    版本：1.0
    日期：2019/7/11
"""


def findindex(char_s, str_d):
    """
        找到字符在字母表中的下标
    """
    index = -1
    for i in range(len(str_d)):
        # print(char_s, str_d[i])
        if char_s == str_d[i]:
            index = i
            break
    return index


def main():
    orign = "abcdefghijklmnopqrstuvwxyz"
    # 大写字母表
    orign_H = orign.upper()
    orign_all = orign + orign_H
    user_msg = input("请输入信息原码(回车结束): ")

    for i in range(len(user_msg)):
        index = findindex(user_msg[i], orign_all)
        # 获得字符下标成功，则按照编码规则进行替换，即替换成该字符在字母表后面第3个字符
        # 大小写字母各自替换，如果是空格或特殊字符则不替换
        if index != -1:
            if index < 26:
                if index + 3 >= 26:
                    print(orign_all[index + 3 - 26], end="")
                else:
                    print(orign_all[index + 3], end="")
            else:
                if index + 3 >= 52:
                    print(orign_all[index + 3 - 26], end="")
                else:
                    print(orign_all[index + 3], end="")
        else:
            print(user_msg[i], end="")


if __name__ == "__main__":
    main()
