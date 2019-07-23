"""
    作者：郑智慧
    版本：1.0
    日期：2019/07/13
    功能：爬取京东商城和亚马逊的商品页面
"""
import requests as rq


def getHtmlText(url):
    """
    爬取网页
    :param url:
    :return:
    """
    try:
        kv = {"user_agent": "Mozilla/5.0"}
        r = rq.get(url, headers=kv, timeout=10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.headers)
        # print(r.text)
    except:
        print("爬取异常")


if __name__ == "__main__":
    # 京东商品页面，可以直接爬取
    url = "https://item.jd.com/100006536488.html"
    # 亚马逊商品页面，需修改user_agent才可以爬取
    url_amazon = "https://www.amazon.com/ref=nav_logo"
    getHtmlText(url_amazon)

