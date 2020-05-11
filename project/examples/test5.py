"""
CPU密集型任务 -- 进程测试

time python process_worker.py

Result [50545553, 50493810, 50511435, 50514261, 50432686, 50449326, 50514232, 50545287]
python process_worker.py  9.88s user 0.08s system 716% cpu 1.391 total
"""
import multiprocessing
from multiprocessing import Pool
import random
from tools import TimeRecord
def compute():
    return sum([random.randint(1, 100) for _ in range(1000000)])
with TimeRecord():
    results=[]
    for i in range(8):
        results.append(compute())
    print(results)