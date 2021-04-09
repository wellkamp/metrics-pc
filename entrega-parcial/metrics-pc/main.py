from dao.GPUMetricsDAO import GPUMetricsDAO
from dao.MemoryMetricsDAO import MemoryMetricDAO
from models.GPUMetrics import GPUMetrics
from models.MemoryMetrics import MemoryMetrics
from models.GPU import GPUModel
from config import connection as conn
import psutil
import time


def main():
    gpu_metrics = GPUMetrics()
    print('Script Rodando....')
    while True:
        try:
            insert_gpu_metrics(get_gpu_temp(gpu_metrics))
            get_memory_metrics()
        except SystemError as e:
            raise print(e)
        time.sleep(600)


def get_gpu_temp(obj):
    gpu_temps = obj.get_temperature_gpu(obj.initialize_openhardwaremonitor())
    return gpu_temps


def insert_gpu_metrics(obj):
    gpu = GPUModel(obj['GPU Core'], obj['GPU Memory'], obj['GPU VRM Core'], obj['GPU Hot Spot'],
                   time.strftime('%Y-%m-%d'), time.strftime('%H:%M:%S'), 1)
    gpu_dao = GPUMetricsDAO(conn.db)
    gpu_dao.insert_gpu_metric(gpu)


def get_memory_metrics():
    memory_metrics = MemoryMetrics(psutil.virtual_memory().percent, psutil.virtual_memory().available,
                                   psutil.virtual_memory().total)
    memory_metrics_dao = MemoryMetricDAO(conn.db)
    memory_metrics_dao.insert_memory_metric(memory_metrics)


if __name__ == '__main__':
    main()