"""
    作者：郑智慧
    版本：1.0
    日期：2019/7/13
    功能：爬取网站首页文本内容
"""
import requests as rq
import time as tm

def getHtmlTxt(url):
    """
    获取网页文本内容
    :param url:
    :return:
    """
    getSuccess = False
    try:
        r = rq.get(url, timeout=5)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        getSuccess = True
    except:
        getSuccess = False
    return getSuccess


if __name__ == "__main__":
    url = "http://www.baidu.com"
    i = 0
    start = tm.perf_counter()
    try_times = 0
    while i < 100:
        # print(getHtmlTxt(url))
        if getHtmlTxt(url):
            try_times = 0
            i += 1
            print("成功爬取{} {}次 {:.2f}s".format(url, i, tm.perf_counter()-start))
        else:
            print("第{}次爬取{}失败,第{}次重试...{:.2f}s".format(i, url, try_times, tm.perf_counter()-start))
            try_times += 1
            if try_times > 10:
                print("尝试次数过多，爬取失败")
                break
    if try_times <= 10:
        print("爬取100次{}的时间是:{:.2f}s".format(url, tm.perf_counter() - start))




