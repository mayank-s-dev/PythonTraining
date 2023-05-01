import time
import psutil


class StatTracker:
    def __init__(self):
        self.stats = []

    def track(self, operation_name, start_time, end_time=None):
        if not end_time:
            end_time = time.time()

        elapsed_time = end_time - start_time
        memory_usage = psutil.Process().memory_info().rss

        self.stats.append({
            "operation_name": operation_name,
            "start_time": start_time,
            "end_time": end_time,
            "elapsed_time": elapsed_time,
            "memory_usage": memory_usage
        })

    def get_stats(self):
        return self.stats

s = StatTracker()
s.track("operation_nameaaaa", time.time())
print(s.stats)