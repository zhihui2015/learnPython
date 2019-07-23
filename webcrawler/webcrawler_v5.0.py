"""
    作者：郑智慧
    版本：1.0
    日期：2019/07/13
    功能：查询IP对应的地区
"""
import requests as rq


def searchIPArea(url, ip):
    """
    查询IP对应的地区
    :param url:
    :return:
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ''Chrome/51.0.2704.63 Safari/537.36'}
    try:
        r = rq.get(url+ip, headers=headers, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text[-3000:-2000])
    except:
        print("查询失败")


if __name__ == "__main__":
    url_ip138 = "http://www.ip138.com/ips138.asp?ip="
    url_ipcn = "https://www.ip.cn/?ip="
    ip = "223.73.193.109"
    searchIPArea(url_ip138, ip)
