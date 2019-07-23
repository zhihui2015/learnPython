"""
    Author: Zheng Zhihui
    Version:0.3
    Date:2019/07/20
    Description: ThreadLocal
"""
import threading


local_student = threading.local()


def pop_name_local():
    name = local_student.name
    print("hello, {} in {}".format(name, threading.current_thread().name))


def push_name_local(name):
    local_student.name = name
    pop_name_local()


def main():
    t1 = threading.Thread(target=push_name_local, args=('Lily', ), name='Thread_A')
    t2 = threading.Thread(target=push_name_local, args=('Tom',), name='Thread_B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("end")


if __name__ == "__main__":
    main()

