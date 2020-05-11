"""
CPU密集型任务 -- 线程测试

Result [50518894, 50451550, 50459412, 50510786, 50502590, 50494441, 50540724, 50479751]
function cost 11.769672870635986.

"""

import threading
import random
from tools import TimeRecord
results = []


def compute():
    results.append(
        sum([random.randint(1, 100) for _ in range(1000000)])
    )

def work_in_thread():
    workers = [threading.Thread(target=compute) for _ in range(8)]
    for work in workers:
        work.start( )
    for work in workers:
        work.join( )
    print(f"Result {results}")
with TimeRecord( ):
    work_in_thread()