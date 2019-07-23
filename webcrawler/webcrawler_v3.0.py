"""
    作者：郑智慧
    版本：1.0
    日期：2019/07/13
    功能：爬取百度和360关键词的页面
"""
import requests as rq


def getHtmlText(url, keyword):
    """
    爬取网页
    :param url:
    :return:
    """
    try:
        # 百度关键词参数
        kv = {"wd": keyword}
        # 360关键词参数
        kv_360 = {"q": keyword}
        r = rq.get(url, params=kv_360)
        r.raise_for_status()
        # print(r.text[:1000])
        print(r.url)
        print(len(r.text))
    except:
        print("爬取异常")


if __name__ == "__main__":
    url = "http://www.baidu.com/s"
    url_360 = "http://www.so.com/s"
    keyword = "python"
    getHtmlText(url_360, keyword)
