"""
    作者：郑智慧
    版本：5.0
    日期：2019/07/16
    功能：AQI计算-requests库
"""
import requests as rq


def get_html_text(url):
    """
        返回url文本
    """
    r = rq.get(url, timeout=30)
    r.encoding = r.apparent_encoding
    return r.text


def main():
    """
        主函数
    """
    city_pinyin = input('请输入城市拼音：')
    url = 'http://www.86pm25.com/city/' + city_pinyin + '.html'
    url_text = get_html_text(url)

    aqi_div = """<tr><th>10时</th><td>"""
    index = url_text.find(aqi_div)
    begin_index = index + len(aqi_div)
    end_index = begin_index + 2
    aqi_val = url_text[begin_index:end_index]
    print(city_pinyin + '10时的空气质量为:{}'.format(aqi_val))


if __name__ == "__main__":
    main()
