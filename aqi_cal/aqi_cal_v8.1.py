"""
    作者：郑智慧
    版本：8.1
    日期：2019/07/16
    功能：AQI计算-requests库 bs4库
"""
import requests as rq
from bs4 import BeautifulSoup
import csv
import re


def get_city_aqi(city_pinyin):
    """
        返回url文本
    """
    url = 'http://www.86pm25.com/' + city_pinyin
    value_list = []
    try:
        r = rq.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, "lxml")
        table_list = soup.find('table')
        tr_list = table_list.find_all('tr')

        div_content = tr_list[1]
        caption = div_content.find_all('td')
        aqi_str = caption[1].text.strip()
        pm25_str = caption[3].text.strip()
        pm10_str = caption[4].text.strip()
        value_list.append(('AQI', aqi_str))
        value_list.append(('PM2.5', pm25_str))
        value_list.append(('PM10', pm10_str))
        # print(value_list)
        return value_list
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

    headers = ['city', 'AQI', 'PM2.5', 'PM10']
    with open("china_city_pm25.csv", 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for i, city in enumerate(city_list):
            if (i+1) % 10 == 0:
                print("已处理{}条记录，共{}条记录".format(i+1, len(city_list)))
            city_name = city[0]
            city_pinyin = city[1]
            value_list = get_city_aqi(city_pinyin)
            city_value = []
            if value_list != -1:
                for value in value_list:
                    if value[1] == '—' or value[1] == '—μg/m³':
                        city_value.append('0')
                    else:
                        value_filter = re.findall(r"\d+\.?\d*", value[1])
                        city_value.append(value_filter[0])
                row = [city_name] + city_value
                print(row)
                writer.writerow(row)
            else:
                print("{}的数据获取失败".format(city_name))


if __name__ == "__main__":
    main()
