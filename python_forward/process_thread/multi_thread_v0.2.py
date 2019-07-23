"""
    Author: Zheng Zhihui
    Version:0.2
    Date:2019/07/20
    Description: Multiple Thread and Lock
"""
import threading


# 创建全局变量，全局变量必须加锁防止多线程修改导致变量不可控
balance = 0
# 创建锁
lock = threading.Lock()


def change_balance(n):
    """
        change balance
    """
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(100000):
        # 上锁
        lock.acquire()
        try:
            change_balance(n)
        finally:
            # 解锁
            lock.release()



def main():
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t3 = threading.Thread(target=run_thread, args=(10,))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print("balance:", balance)


if __name__ == "__main__":
    main()

