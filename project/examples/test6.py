# thread_worker_with_future.py
"""
Result [50523964, 50551644, 50524813, 50513045, 50494442, 50478434, 50502136, 50479842]
time cost: 11.787674188613892.
"""
import random
import threading
from tools import TimeRecord
from concurrent import futures

def compute():
    return sum([random.randint(1, 100) for _ in range (1000000)])

with TimeRecord( ):
    with futures.ThreadPoolExecutor(8) as executor:
        todo = [executor.submit(compute) for _ in range(8)]

    results = []
    for future in futures.as_completed(todo):
        res = future.result()
        results.append(res)

    print(f"Result {results}")