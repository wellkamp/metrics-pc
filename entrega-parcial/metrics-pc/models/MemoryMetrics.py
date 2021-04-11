import time


class MemoryMetrics():
    def __init__(self, percent, available, total, pc_id):
        self._percent = percent
        self._available = available
        self._total = total
        self._created_at = time.strftime('%Y-%m-%d')
        self._hour_at = time.strftime('%H:%M:%S')
        self._pc_id = pc_id

    @property
    def percent(self):
        return self._percent

    @property
    def available(self):
        return round(self._available * 100 / self._total, 1)

    @property
    def created_at(self):
        return self._created_at

    @property
    def hour_at(self):
        return self._hour_at

    @property
    def pc_id(self):
        return self._pc_id