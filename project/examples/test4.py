"""
CPU密集型任务 -- 进程测试

[50492814, 50485302, 50493930, 50502064, 50527312, 50525403, 50498831, 50474334]
function cost 5.98234224319458.

"""
import time
import multiprocessing
from multiprocessing import Pool
import random
from tools import TimeRecord


def compute(n):
    return sum([random.randint(1, 100) for _ in range(1000000)])
    # return sum([random.randint(1, 100) for _ in range(10)])

if __name__ == '__main__':
    # print('__name__',{__name__})
    with Pool(6) as p:
        with TimeRecord( ):
            print(p.map(compute, range(8)))
