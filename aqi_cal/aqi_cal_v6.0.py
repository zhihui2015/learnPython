"""
    作者：郑智慧
    版本：6.0
    日期：2019/07/16
    功能：AQI计算-requests库 bs4库
"""
import requests as rq
from bs4 import BeautifulSoup


def get_city_aqi(city_pinyin):
    """
        返回url文本
    """
    url = 'http://www.86pm25.com/city/' + city_pinyin + '.html'
    try:
        r = rq.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, "lxml")
        table_list = soup.find('table')
        tr_list = table_list.find_all('tr')

        pm25_dict = {}
        for i in range(1, 9):
            div_content = tr_list[i]
            caption = div_content.find_all('td')
            pm25_dict[caption[0].string] = caption[3].text.strip()
        return pm25_dict
    except:
        print("爬取失败:", r.status_code)
    return r.text


def main():
    """
        主函数
    """
    city_pinyin = input('请输入城市拼音：')
    pm25_dict = get_city_aqi(city_pinyin)
    print("各个城区的PM2.5是: ", pm25_dict)


if __name__ == "__main__":
    main()
