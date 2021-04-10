import clr as pythonnet


class GPUMetrics():
    def __init__(self, lib):
        self._lib = lib

    def initialize_openhardwaremonitor(self):
        """Incializa a lib retornando o objeto Computer"""
        pythonnet.AddReference(self._lib)

        from OpenHardwareMonitor import Hardware

        handle = Hardware.Computer()
        handle.GPUEnabled = True
        handle.Open()
        return handle

    def get_temperature_gpu(self, handle):
        """Retorna um dicionario com a temperatura da placa de video"""
        temps = {}
        gpu_index_enabled = 0
        for i in range(0, 6):
            temps[handle.Hardware[gpu_index_enabled].Sensors[i].get_Name()] = handle.Hardware[gpu_index_enabled].Sensors[i].get_Value()
        return temps