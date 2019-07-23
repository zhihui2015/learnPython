"""
    作者：郑智慧
    版本：3.0
    日期：2019/07/17
    功能：AQI计算-csv格式对应list
"""
import json
import csv


def process_json_file(filepath):
    """
        解码json文件
    """
    f = open(filepath, mode='r', encoding='utf-8')
    city_list = json.load(f)
    return city_list



def main():
    """
        主函数
    """
    filepath = input('请输入json文件名称: ')
    city_list = process_json_file(filepath)
    city_list.sort(key=lambda city: city['aqi'])
    # print(list(city_list[0].keys()))
    lines = []
    lines.append(list(city_list[0].keys()))
    for city in city_list:
        lines.append(list(city.values()))

    f = open('aqi.csv', mode='w', encoding='utf-8', newline='')
    writer = csv.writer(f)
    for line in lines:
        writer.writerow(line)
    f.close()




if __name__ == "__main__":
    main()





