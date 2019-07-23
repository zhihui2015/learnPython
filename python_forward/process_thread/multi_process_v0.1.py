"""
    作者：郑智慧
    版本：0.1
    日期：2019/07/19
    功能：multiprocessing库导入Process方法
"""
import os
from multiprocessing import Process


def run_proc(name):
    """
        进程执行
    """
    print('Run child process %s (%s)...' % (name, os.getpid()))


def main():
    print("Process %s start...", os.getpid())
    p = Process(target=run_proc, args=('proc_1',))
    print("child process start")
    p.start()
    p.join()
    print("child process end")


if __name__ == "__main__":
    main()


