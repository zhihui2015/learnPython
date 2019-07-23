"""
    作者：郑智慧
    版本：10.0
    日期：2019/07/16
    功能：AQI计算-pandas
"""
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    """
        主函数
    """
    aqi_data = pd.read_csv("china_city_pm25.csv")
    print("基本信息：")
    print(aqi_data.info())

    print("数据预览：")
    print(aqi_data.head())

    # pandas数据清洗
    # 只保留AQI>0的数据
    # filter_condition = aqi_data['AQI'] > 0
    # clean_aqi_data = aqi_data[filter_condition]
    clean_aqi_data = aqi_data[aqi_data['AQI'] > 0]

    print("AQI最大值：", clean_aqi_data['AQI'].max())
    print("AQI最小值：", clean_aqi_data['AQI'].min())
    print("AQI的平均值：", clean_aqi_data['AQI'].mean())

    # pandas数据可视化
    top50_cities = clean_aqi_data.sort_values(by=['AQI']).head(50)
    top50_cities.plot(kind='dot', x='city', y='AQI', title='空气质量最好的50个城市',
                      figsize=(20, 20))
    plt.savefig('top50_aqi_bar.png')
    plt.show()


if __name__ == "__main__":
    main()
