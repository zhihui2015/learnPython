"""
    作者：郑志汇
    功能：温度转换
    版本：1.0
    日期：2019/7/6

"""

TempStr = input('请输入带有符号的温度值：')
if TempStr[-1] in ['F','f']:
    C = (eval(TempStr[0:-1]) - 32) / 1.8
    print('转换后的温度是{: .2f}C'.format(C))
elif TempStr[-1] in ['C', 'c']:
    F = 1.8 * eval(TempStr[0:-1]) + 32
    print('转换后的温度是{: .2f}F'.format(F))
else:
    print('输入格式错误')


