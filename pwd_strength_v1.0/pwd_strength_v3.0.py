"""
    作者：郑智慧
    版本：3.0
    日期：2019/7/13
    功能：判断密码强度
    2.0功能：循环和终止
    3.0功能：将密码保存到文本中
"""
import time as tm


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
    pwd_strength_dict = {0: '弱', 1: '较弱', 2: '中', 3: '强'}
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

        now_time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
        with open("password_3.0.txt", 'a') as f:
            f.write("日期:{} 密码:{} 强度:{}{}\n".format(now_time, password,
                                                   password_strength, pwd_strength_dict[password_strength]))

        # try:
        #     f = open("password_3.0.txt", 'a')
        #     f.write(password + '\n')
        #     print("写入成功")
        # except:
        #     print("写入异常")
        # finally:
        #     f.close()

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

