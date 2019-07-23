"""
    作者：郑智慧
    版本：2.0
    日期：2019/7/13
    功能：判断密码强度
    2.0功能：循环和终止
"""


def check_number_exist(password_str):
    """
    判断密码中是否含数字
    :param password:
    :return:
    """
    has_number = False
    for c in password_str:
        if c.isnumeric():
            has_number = True
            break
    return has_number


def check_alpha_exist(password_str):
    """
    判断字母是否存在
    :param password_str:
    :return:
    """
    has_alpha = False
    for c in password_str:
        if c.isalpha():
            has_alpha = True
            break
    return has_alpha


def main():
    """
    主函数
    :return:
    """
    try_times = 5

    while try_times > 0:
        password = input('请输入密码: ')
        password_strength = 0

        # 规则1：长度至少8位
        if len(password) >= 8:
            password_strength += 1
        else:
            print('密码长度至少8位')

        # 规则2：必须包含数字
        if check_number_exist(password):
            password_strength += 1
        else:
            print('密码需要包含数字')

        # 规则3：必须包含字母
        if check_alpha_exist(password):
            password_strength += 1
        else:
            print('密码需要包含字母')

        if password_strength >= 3:
            print('恭喜！密码合格')
            break
        else:
            print('密码不合格')
            try_times -= 1
            print()
    if try_times <= 0:
        print('尝试次数过多，密码设置失败!')


if __name__ == "__main__":
    main()

