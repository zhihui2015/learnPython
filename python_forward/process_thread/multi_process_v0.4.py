"""
    作者：郑智慧
    版本：0.4
    日期：2019/07/19
    功能：分布式进程-master
"""
import random, queue
from multiprocessing.managers import BaseManager


task_quene = queue.Queue()
result_quene = queue.Queue()


class QueneManager(BaseManager):
    pass


def get_task_quene():
    global task_quene
    return task_quene


def get_result_quene():
    global result_quene
    return result_quene


def main():
    QueneManager.register('get_task_quene', callable=get_task_quene)
    QueneManager.register('get_result_quene', callable=get_result_quene)
    manager = QueneManager(address=('127.0.0.1', 5000), authkey=b'abc')
    manager.start()
    task = manager.get_task_quene()
    result = manager.get_result_quene()
    for i in range(10):
        n = random.randint(1, 10000)
        task.put(n)
        print("put task %s" % n)

    print("try get result")
    for i in range(10):
        try:
            r = result.get(timeout=10)
            print("result %s" % r)
        except queue.Empty:
            print("队列中没有数据")
    manager.shutdown()
    print("master exit")


if __name__ == "__main__":
    main()


