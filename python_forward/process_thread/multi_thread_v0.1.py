"""
    作者：郑智慧
    版本：0.1
    日期：2019/07/20
    功能：多线程
"""
import time, threading


def loop():
    print("thread {} is running".format(threading.current_thread().name))
    for i in range(5):
        print("thread {}>>>{}".format(threading.current_thread().name, i))
        time.sleep(1)
    print("thread {} end".format(threading.current_thread().name))


def main():
    print("thread {} is running".format(threading.current_thread().name))
    # 创建线程，指定线程的任务函数和任务名
    t = threading.Thread(target=loop, name='loopthread')
    # 启动线程
    t.start()
    # join的作用：线程结束后可以继续往下执行，类似于信号量，常用于线程通信
    t.join()
    print("thread {} end".format(threading.current_thread().name))


if __name__ == "__main__":
    main()
