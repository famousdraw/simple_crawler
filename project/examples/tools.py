import time
class TimeRecord:

    def __init__(self):
        self._start = 0
        self._end = 0

    def __enter__(self):
        self._start = time.time( )

    def __exit__(self, exc_type, exc_value, traceback):
        self._end = time.time( )
        print(f"time cost: {self._end - self._start}.")