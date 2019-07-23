"""
    作者：Zheng Zhihui
    功能：汇率兑换
    版本：3.0
    日期：2019/7/8
    2.0 新增功能：根据输入判断是人民币还是美元，进行相应的患上计算
    3.0 新增功能：程序可以一直运行，知道用户退出
"""

# 汇率
USD_VS_RMB = 6.77

# 带单位的货币的输入
currency_str_value = input('请输入带单位的货币金额(退出程序请按Q)：')

while currency_str_value != 'Q':
    # 获取货币单位
    unit = currency_str_value[-3:]

    if unit in ['CNY']:
        rmb_str_value = currency_str_value[:-3]
        rmb_value = eval(rmb_str_value)
        usd_value = rmb_value / USD_VS_RMB
        print('你输入的是人民币', rmb_value, '转换后的美元是{:.2f}USD'.format(usd_value))
    elif unit in ['USD']:
        usd_str_value = currency_str_value[:-3]
        usd_value = eval(usd_str_value)
        rmb_value = usd_value * USD_VS_RMB
        print('你输入的是美元', usd_value, '转换后的人民币是{:.2f}CNY'.format(rmb_value))
    else:
        print('输入的货币不支持')

    print('*************************************************************')
    # 带单位的货币的输入
    currency_str_value = input('请输入带单位的货币金额(退出程序请按Q)：')

print('程序已退出')



