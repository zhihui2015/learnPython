"""
    作者：郑智慧
    版本：2.0
    日期：2019/07/13
    功能：凯撒密码
"""

def main():
    """
        主函数
    """
    str_origin = input("请输入信息原码(回车结束): ")
    str_coded = ""

    for c in str_origin:
        if 'a' <= c <= 'z':
            str_coded += chr(ord('a') + (ord(c) - ord('a') + 3) % 26)
        elif 'A'<= c <= 'Z':
            str_coded += chr(ord('A') + (ord(c) - ord('A') + 3) % 26)
        else:
            str_coded += c
    print("编码后是: ", str_coded)


if __name__ == "__main__":
    main()
