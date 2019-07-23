"""
    作者：郑智慧
    版本：7.0
    日期：2019/7/13
    功能：判断密码强度
    2.0功能：循环和终止
    3.0功能：将密码保存到文本中
    4.0功能：读取文件，遍历文件
    5.0功能：定义PasswordTool类
    6.0功能：定义FileTool类
    7.0功能：密码中增加大小写字母和特殊字符“+，-，*，/”
"""
import time as tm


class FileTool():
    """
        文件工具类
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

    def check_letter_exist(self):
        """
            判断是否含字母
        """
        has_upper_letter = False
        has_lower_letter = False
        for c in self.password:
            if c.isupper():
                has_upper_letter = True
            elif c.islower():
                has_lower_letter = True
            has_both_letter = has_upper_letter and has_lower_letter
            if has_both_letter:
                break
        return has_both_letter

    def check_specialchar_exist(self):
        """
            判断是否包含特殊字符
        """
        has_specialchar = False
        specialchar_list = ['+', '-', '*', '/', '_', '&', '%', ',']
        for c in self.password:
            if c in specialchar_list:
                has_specialchar = True
                break
        return has_specialchar

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

        # 规则3：必须包含大小写字母
        if self.check_letter_exist():
            self.strength_level += 1
        else:
            print('密码需要包含大小写字母')

        # 规则4：需要包含特殊字符
        if self.check_specialchar_exist():
            self.strength_level += 1
        else:
            print('密码需要包含至少一个特殊字符("+,-,*,/,_")')


def main():
    """
        主函数
    """
    try_times = 5
    pwd_strength_dict = {0: '弱', 1: '较弱', 2: '中', 3: '强', 4: '超强'}
    myfile = FileTool("password_7.0.txt")

    while try_times > 0:
        password = input('请输入密码: ')
        mypwdtool = PasswordTool(password)
        mypwdtool.process_password()

        now_time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
        myfile.write_to_file("日期:{} 密码:{} 强度:{}{}\n".format(now_time, password,
                                                   mypwdtool.strength_level, pwd_strength_dict[mypwdtool.strength_level]))

        if mypwdtool.strength_level >= 4:
            print('恭喜！密码合格')
            break
        else:
            print('密码不合格')
            try_times -= 1
            print()
    if try_times <= 0:
        print('尝试次数过多，密码设置失败!')

    content = myfile.read_from_file()
    print(content)


if __name__ == "__main__":
    main()


