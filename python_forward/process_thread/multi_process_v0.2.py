"""
    作者：郑智慧
    版本：0.2
    日期：2019/07/19
    功能：multiprocessing库导入Pool方法
"""
import os, time, random
from multiprocessing import Pool


def long_time_task(name):
    print("task %s (%s)" % (name, os.getpid()))
    start = time.perf_counter()
    time.sleep(random.random())
    end = time.perf_counter()
    print("task {} run {:.2f}".format(name, end-start))


def main():
    print("parent process {} start".format(os.getpid()))
    # Pool的参数如果不填则默认是4
    p = Pool()
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print("waiting all subprocess done")
    p.close()
    p.join()
    print("all subprocess done")


if __name__ == "__main__":
    main()


