"""
    作者：郑智慧
    版本：5.0
    日期：2019/7/13
    功能：判断密码强度
    2.0功能：循环和终止
    3.0功能：将密码保存到文本中
    4.0功能：读取文件，遍历文件
    5.0功能：相关函数封装为类
"""
import time as tm


class PasswordTool():
    """
        密码工具类
    """
    def __init__(self, password):
        self.password = password
        self.strength_level = 0

    def check_number_exist(self):
        """
            判断是否含数字
        """
        has_number = False
        for c in self.password:
            if c.isnumeric():
                has_number = True
                break
        return has_number

    def check_alpha_exist(self):
        """
            判断是否含字母
        """
        has_alpha = False
        for c in self.password:
            if c.isalpha():
                has_alpha = True
                break
        return has_alpha

    def process_password(self):
        """
            判断是否符合规则
        """
        # 规则1：长度至少8位
        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            print('密码长度至少8位')

        # 规则2：必须包含数字
        if self.check_number_exist():
            self.strength_level += 1
        else:
            print('密码需要包含数字')

        # 规则3：必须包含字母
        if self.check_alpha_exist():
            self.strength_level += 1
        else:
            print('密码需要包含字母')


def main():
    """
    主函数
    :return:
    """
    try_times = 5
    pwd_strength_dict = {0: '弱', 1: '较弱', 2: '中', 3: '强'}
    while try_times > 0:
        password = input('请输入密码: ')
        mypwdtool = PasswordTool(password)
        mypwdtool.process_password()

        now_time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
        with open("password_5.0.txt", 'a') as f:
            f.write("日期:{} 密码:{} 强度:{}{}\n".format(now_time, password,
                                                   mypwdtool.strength_level, pwd_strength_dict[mypwdtool.strength_level]))

        if mypwdtool.strength_level >= 3:
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

