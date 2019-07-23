"""
    作者：郑智慧
    版本：9.0
    日期：2019/07/16
    功能：AQI计算-pandas
"""
import pandas as pd


def main():
    """
        主函数
    """
    aqi_data = pd.read_csv("china_city_pm25.csv")
    print("基本信息：")
    print(aqi_data.info())

    print("数据预览：")
    print(aqi_data.head())

    # 数据清洗
    # 只保留AQI>0的数据
    # filter_condition = aqi_data['AQI'] > 0
    # clean_aqi_data = aqi_data[filter_condition]
    clean_aqi_data = aqi_data[aqi_data['AQI'] > 0]

    print("AQI最大值：", clean_aqi_data['AQI'].max())
    print("AQI最小值：", clean_aqi_data['AQI'].min())
    print("AQI的平均值：", clean_aqi_data['AQI'].mean())

    top10_cities = clean_aqi_data.sort_values(by=['AQI']).head(10)
    print("空气最好的10个城市：")
    print(top10_cities)

    # bottom10_cities = clean_aqi_data.sort_values(by=['AQI']).tail(10)
    bottom10_cities = clean_aqi_data.sort_values(by=['AQI'], ascending=False).head(10)
    print("空气最差的10个城市：")
    print(bottom10_cities)

    top10_cities.to_csv("top10_pm25.csv", index=False)
    bottom10_cities.to_csv("bottom10_pm25.csv", index=False)


if __name__ == "__main__":
    main()
