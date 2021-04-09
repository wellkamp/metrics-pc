SQL_INSERT_SENSOR = 'INSERT INTO ' \
                    'personalmetrics_gpumetrics (gpu_core, gpu_memory, gpu_vrm_core, gpu_hot_spot, created_at, hour_at, pc_id) ' \
                    'VALUES (%s, %s, %s, %s, %s, %s, %s)'


class GPUMetricsDAO():
    def __init__(self, db):
        self.db = db

    def insert_gpu_metric(self, obj):
        cursor = self.db.cursor()
        cursor.execute(SQL_INSERT_SENSOR, (obj.gpu_core, obj.gpu_memory, obj.gpu_vrm_core,
                                           obj.gpu_hot_spot, obj.created_at, obj.hour_at, obj.pc_id))
        cursor.close()