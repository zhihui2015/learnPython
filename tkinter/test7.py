from random import random
from math import sqrt
import time

DARTS = 10
hits = 0.0
time.process_time()

for i in range(1, DARTS):
    x, y = random(), random()
    dist = sqrt(x**2 + y**2)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * hits / DARTS
print("Π的值是:", pi)
print("程序运行的时间是:", time.process_time())





