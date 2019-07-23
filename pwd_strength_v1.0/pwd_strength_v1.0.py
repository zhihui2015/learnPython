"""
    作者：郑智慧
    版本：1.0
    日期：2019/7/13
    功能：判断密码强度
"""


def check_number_exist(password_str):
    """
    判断密码中是否含数字
    :param password:
    :return:
    """
    for c in password_str:
        if c.isnumeric():
            return True
    return False


def check_alpha_exist(password_str):
    for c in password_str:
        if c.isalpha():
            return True
    return False


def main():
    """
    主函数
    :return:
    """
    password = input('请输入密码: ')
    password_strength = 0

    if len(password) >= 8:
        password_strength += 1
    else:
        print('密码长度至少8位')

    if check_number_exist(password):
        password_strength += 1
    else:
        print('密码需要包含数字')

    if check_alpha_exist(password):
        password_strength += 1
    else:
        print('密码需要包含字母')

    if password_strength >= 3:
        print('恭喜！密码合格')
    else:
        print('密码不合格')

if __name__ == "__main__":
    main()

