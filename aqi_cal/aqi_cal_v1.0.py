"""
    作者：郑智慧
    版本：1.0
    日期：2019/07/16
    功能：AQI计算-复习之前的课程内容
"""


def cal_linear(iaqi_lo, iaqi_hi, bp_lo, bp_hi, cp):
    """
        范围缩放
    """
    iaqi = (iaqi_hi - iaqi_lo) * (cp - bp_lo) / (bp_hi - bp_lo) + iaqi_lo
    return iaqi


def cal_pm_iaqi(pm_val):
    """
        计算PM2.5的AQI
    """
    if 0 <= pm_val < 36:
        iaqi = cal_linear(0, 50, 0, 35, pm_val)
    elif 26 <= pm_val < 76:
        iaqi = cal_linear(50, 100, 35, 75, pm_val)
    elif 76 <= pm_val < 116:
        iaqi = cal_linear(100, 150, 75, 115)
    else:
        pass
    return iaqi


def cal_co_iaqi(co_val):
    """
        计算CO的AQI
    """
    if 0 <= co_val < 3:
        iaqi = cal_linear(0, 50, 0, 3, co_val)
    elif 3 <= co_val < 5:
        iaqi = cal_linear(50, 100, 2, 4, co_val)
    else:
        pass
    return iaqi


def cal_aqi(param_list):
    """
        AQi计算
    """
    pm_val = param_list[0]
    co_val = param_list[1]

    pm_iaqi = cal_pm_iaqi(pm_val)
    co_iaqi = cal_co_iaqi(co_val)

    iaqi_list = []
    iaqi_list.append(pm_iaqi)
    iaqi_list.append(co_iaqi)

    aqi = max(iaqi_list)
    return aqi


def main():
    """
        主函数
    """
    print("请输入以下信息，用空格分隔")
    input_str = input("(1)PM2.5 (2)CO: ")
    str_list = input_str.split(' ')
    pm_value = float(str_list[0])
    co_value = float(str_list[1])

    param_list = []
    param_list.append(pm_value)
    param_list.append(co_value)
    print(param_list)
    # 调用aqi计算函数
    aqi_value = cal_aqi(param_list)
    print("AQI指数是: ", aqi_value)


if __name__ == "__main__":
    main()
