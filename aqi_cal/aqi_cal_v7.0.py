"""
    作者：郑智慧
    版本：7.0
    日期：2019/07/16
    功能：AQI计算-requests库 bs4库
"""
import requests as rq
from bs4 import BeautifulSoup


def get_city_aqi(city_pinyin):
    """
        返回url文本
    """
    url = 'http://www.86pm25.com/' + city_pinyin
    try:
        r = rq.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, "lxml")
        table_list = soup.find('table')
        tr_list = table_list.find_all('tr')

        div_content = tr_list[1]
        caption = div_content.find_all('td')
        return caption[3].text.strip()

        # pm25_dict = {}
        # for i in range(1, 2):
        #     div_content = tr_list[i]
        #     caption = div_content.find_all('td')
        #     pm25_dict[caption[0].string] = caption[3].text.strip()
        # return pm25_dict
    except:
        print("爬取失败:", r.status_code)
    return -1


def get_all_cities():
    """
        获取所有城市
    """
    url = "http://www.86pm25.com/"
    city_list = []
    try:
        r = rq.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, 'html.parser')

        city_div = soup.find_all('div', {'class': 'aqi-site'})[1]
        city_link_list =city_div.find_all('a')
        for city_link in city_link_list:
            city_name = city_link.text
            city_pinyin = city_link['href']
            city_list.append((city_name, city_pinyin))
        return city_list
    except:
        print("爬取失败")
    return -1


def main():
    """
        主函数
    """
    city_list = get_all_cities()
    for city in city_list:
        city_name = city[0]
        city_pinyin = city[1]
        aqi_value = get_city_aqi(city_pinyin)
        print("{}的PM2.5是: {}".format(city_name, aqi_value))



if __name__ == "__main__":
    main()
