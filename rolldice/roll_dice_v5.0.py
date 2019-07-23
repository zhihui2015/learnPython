"""
    作者：郑智慧
    版本：0.5
    日期：2019/07/15
    功能：模拟摇骰子-list+random
    0.2功能：模拟两个骰子-dict+random
    0.3功能：投掷骰子数据可视化-matplotlib
    0.4功能：对结果进行数据统计和分析
    0.5功能：使用科学计算库-NumPy
"""
import numpy as np
import matplotlib.pyplot as plt

# 解决中文在pyplot上的显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    """
        主函数
    """
    total_times = 10000

    # 记录骰子结果
    roll1_arr = np.random.randint(1, 7, size=total_times)
    roll2_arr = np.random.randint(1, 7, size=total_times)
    result_arr = roll1_arr + roll2_arr

    # 直方图数据输出
    hist, bins = np.histogram(result_arr, bins=range(2, 14))
    print(hist)
    print(bins)

    # 绘制直方图
    plt.hist(result_arr, bins=range(2, 14), density=1, edgecolor='black', linewidth=1, rwidth=0.8)
    # 设置x轴坐标点
    ticks_lables = ['2点', '3点', '4点', '5点',
                    '6点', '7点', '8点', '9点', '10点', '11点', '12点']
    ticks_pos = np.arange(2, 13) + 0.5
    plt.xticks(ticks_pos, ticks_lables)

    plt.title("骰子点数统计")
    plt.xlabel("点数")
    plt.ylabel("频率")
    plt.ylabel("频率")
    plt.show()


if __name__ == "__main__":
    main()


