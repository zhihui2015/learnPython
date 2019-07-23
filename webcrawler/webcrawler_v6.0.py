"""
    作者：郑智慧
    版本：6.0
    日期：2019/07/16
    功能：使用beautifulsoup库解析网页内容(本代码用来爬取txt文件)
"""
import requests as rq
from bs4 import BeautifulSoup


def main():
    """
        主函数
    """
    # demo
    url1 = "https://python123.io/ws/demo.html"
    # 蛙-莫言
    url2 = "https://www.kanunu8.com/book3/8257/"
    # 我的名字叫红
    url3 = "https://www.kanunu8.com/book3/7515/"
    # 修道院纪事
    url4 = "https://www.kanunu8.com/book3/8128/"
    print("请输入以下信息，用空格分隔:")
    book_str = input("(1)网址 (2)起始页 (3)结束页 (4)文件名: ")
    try:
        book_list = book_str.split(" ")
        begin_page = int(book_list[1])
        end_page = int(book_list[2])
        filename = book_list[3]
        for i in range(begin_page, end_page+1):
            r = rq.get(book_list[0]+str(i)+".html", timeout=30)
            r.encoding = r.apparent_encoding
            demo = r.text
            soup = BeautifulSoup(demo, "html.parser")
            # print(soup.title.string)
            # print(soup.p.get_text())

            with open(filename, mode='a', encoding='utf-8') as f:
                f.write("第{}章\n".format(i-begin_page) + soup.p.get_text() + '\n\n\n')
                print("第{}章 完成".format(i-begin_page))
    except:
        print("输入格式错误")


if __name__ == "__main__":
    main()
