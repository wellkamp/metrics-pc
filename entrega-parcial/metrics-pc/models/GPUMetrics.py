import clr


class GPUMetrics():
    def __init__(self):
        self.lib = r'B:\API\metrics-api\helpers\OpenHardwareMonitorLib.dll'

    def initialize_openhardwaremonitor(self):
        """Incializa a lib retornando o objeto Computer"""
        clr.AddReference(self.lib)

        from OpenHardwareMonitor import Hardware

        handle = Hardware.Computer()
        handle.GPUEnabled = True
        handle.Open()
        return handle

    def get_temperature_gpu(self, handle):
        """Retorna um dicionario com a temperatura da placa de video"""
        temps = {}
        for i in range(0, 6):
            temps[handle.Hardware[0].Sensors[i].get_Name()] = handle.Hardware[0].Sensors[i].get_Value()
        return temps