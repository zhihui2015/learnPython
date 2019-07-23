"""
    作者：郑智慧
    版本：4.0
    日期：2019/07/17
    功能：AQI计算-根据输入的文件判断是json还是csv，使用os模块
"""
import json
import csv
import os


def process_json_file(filepath):
    """
        解码json文件
    """
    with open(filepath, mode='r', encoding='utf-8') as f:
        city_list = json.load(f)
    print(city_list)


def process_csv_file(filepath):
    """
        处理csv文件
    """
    with open(filepath, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(','.join(row))


def main():
    """
        主函数
    """
    filepath = input('请输入json文件名称: ')
    filename, file_ext = os.path.splitext(filepath)

    if file_ext == '.json':
        process_json_file(filepath)
    elif file_ext == '.csv':
        process_csv_file(filepath)
    else:
        print('不支持的文件格式')


if __name__ == "__main__":
    main()





