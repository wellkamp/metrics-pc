from models.MemoryMetrics import MemoryMetrics

SQL_INSERT_SENSOR = 'INSERT INTO ' \
                    'personalmetrics_memorymetrics (used, available, created_at, hour_at, pc_id) ' \
                    'VALUES (%s, %s, %s, %s, %s)'


class MemoryMetricDAO():
    def __init__(self, db):
        self.db = db

    def insert_memory_metric(self, obj):
        if isinstance(obj, MemoryMetrics):
            cursor = self.db.cursor()
            cursor.execute(SQL_INSERT_SENSOR, (obj.percent, obj.available, obj.created_at, obj.hour_at, obj.pc_id))
            self.db.commit()
        else:
            print('Não é instancia')