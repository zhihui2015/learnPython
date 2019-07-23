"""
    作者：郑智慧
    版本：0.4
    日期：2019/07/19
    功能：分布式进程-worker
"""
import queue, time
from multiprocessing.managers import BaseManager


class QueneManager(BaseManager):
    pass


def main():
    QueneManager.register('get_task_quene')
    QueneManager.register('get_result_quene')
    m = QueneManager(address=('127.0.0.1', 5000), authkey=b'abc')
    m.connect()
    task = m.get_task_quene()
    result = m.get_result_quene()

    for i in range(10):
        try:
            n = task.get(timeout=10)
            r = n * n
            print("get master's data and run task %d * %d = %d" % (n, n, r))
            time.sleep(1)
            result.put(r)
        except queue.Empty:
            print("队列中没有数据")
    print("worker exit")


if __name__ == "__main__":
    main()


