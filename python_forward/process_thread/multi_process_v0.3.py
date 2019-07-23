"""
    作者：郑智慧
    版本：0.3
    日期：2019/07/19
    功能：使用Quene来使进程通信
"""
import os, time, random
from multiprocessing import Process, Queue


def push_quene(quene):
    """
        数据入队列中
    """
    print("task id {} - push".format(os.getpid()))
    for value in ['A', 'B', 'C']:
        # 数据入队列
        quene.put(value)
        print("push {} to quene".format(value))
        time.sleep(random.random())


def pop_quene(quene):
    """
        推数据出队列
    """
    print("task id {} - pop".format(os.getpid()))
    while True:
        # 数据出队列
        value = quene.get()
        print("get {} in quene".format(value))


def main():
    # 创建队列
    q = Queue()
    # 创建入队列和出队列两个进程
    p_push = Process(target=push_quene, args=(q,))
    p_pop = Process(target=pop_quene, args=(q,))
    # 启动进程
    p_push.start()
    p_pop.start()
    # 等待进程结束，pop经常由于有死循环所有用terminate
    p_push.join()
    p_pop.terminate()


if __name__ == "__main__":
    main()


