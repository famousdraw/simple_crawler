"""
CPU密集型任务 -- 线程测试

time python thread_worker.py

Result [50584212, 50486575, 50481798, 50460655, 50567586, 50463214, 50522043]
python thread_work.py  5.75s user 0.08s system 100% cpu 5.830 total
"""

import threading
import random

results = []


def compute():
    results.append(
        sum([random.randint(1, 100) for _ in range(1000000)])
    )


workers = [threading.Thread(target=compute) for _ in range(8)]

for work in workers:
    work.start( )

for work in workers:
    work.join( )

print(f"Result {results}")