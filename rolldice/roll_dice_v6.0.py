"""
    作者：郑智慧
    版本：0.6
    日期：2019/07/15
    功能：使用matplotlib和numpy库分析投掷3个骰子时和的频率分布
"""
import matplotlib.pyplot as plt
import numpy as np


# 解决中文在pyplot上的显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    """
        主函数
    """
    total_times = 10000
    roll1_list = np.random.randint(1, 7, size=total_times)
    # print(roll1_list)
    roll2_list = np.random.randint(1, 7, size=total_times)
    # print(roll2_list)
    roll3_list = np.random.randint(1, 7, size=total_times)
    # print(roll3_list)

    result_list = roll1_list + roll2_list + roll3_list
    # print(result_list)

    hist, bins = np.histogram(result_list, bins=range(3, 21))
    print(hist)
    print(bins)

    # 绘制直方图
    plt.hist(result_list, bins=range(3, 21), density=1, linewidth=1, rwidth=0.9)
    # 设置x轴坐标点
    ticks_lables = ['3点', '4点', '5点', '6点', '7点', '8点', '9点',
                    '10点', '11点', '12点', '13点', '14点', '15点',
                    '16点', '17点', '18点']
    ticks_pos = np.arange(3, 21) + 0.5
    plt.xticks(ticks_pos, ticks_lables)

    plt.title("骰子点数统计")
    plt.xlabel("点数")
    plt.ylabel("频率")
    plt.ylabel("频率")
    plt.show()


if __name__ == "__main__":
    main()
