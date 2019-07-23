"""
    作者：郑智慧
    功能：幂运算，天天向上的力量
    版本：1.0
    日期：2019/7/10
"""


def workdayUpCount(dayfactor):
    """

    """
    dayup = 1
    for i in range(365):
        if i % 5 in [3, 4]:
            dayup *= (1 - 0.01)
        else:
            dayup *= (1 + dayfactor)
    # print("工作日的力量{:.3f}".format(dayup))
    return dayup


def main():
    """
        主函数
    """
    daydayup = pow(1.01, 365)
    print("天天向上的力量{:.3f}".format(daydayup))

    dayfactor = 0.01
    while workdayUpCount(dayfactor) < daydayup:
        dayfactor += 0.001


    print("工作日的力量系数{:.3f}".format(dayfactor))




if __name__ == "__main__":
    main()



