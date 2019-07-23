"""
    作者：郑智慧
    功能：设计一个进度条
    版本：1.0
    日期：2019.7.11
"""
import time as tm


def main():
    scale = 10
    start = tm.perf_counter()
    print("执行开始".center(scale//2, '-'))
    for i in range(scale + 1):
        done = '*' * i
        undone = '.' * (scale - i)
        rate = i / scale * 100

        dur = tm.perf_counter() - start
        print("\r{:>3.0f}% [{}->{}] {:.2f}s".format(rate, done, undone, dur), end="")
        tm.sleep(0.1)
    print("\n" + "执行结束".center(scale // 2, '-'))


if __name__ == "__main__":
    main()
