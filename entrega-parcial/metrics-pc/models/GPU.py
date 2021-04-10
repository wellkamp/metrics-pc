import time

class GPUModel():
    def __init__(self, gpu_core, gpu_memory, gpu_vrm_core, gpu_hot_spot, pc_id):
        self._gpu_core = gpu_core
        self._gpu_memory = gpu_memory
        self._gpu_vrm_core = gpu_vrm_core
        self._gpu_hot_spot = gpu_hot_spot
        self._created_at = time.strftime('%Y-%m-%d')
        self._hour_at = time.strftime('%H:%M:%S')
        self._pc_id = pc_id

    @property
    def hour_at(self):
        return self._hour_at

    @hour_at.setter
    def hour_at(self, hour_at):
        self._hour_at = hour_at

    @property
    def gpu_core(self):
        return self._gpu_core

    @gpu_core.setter
    def gpu_core(self, gpu_core):
        self._gpu_core = gpu_core

    @property
    def gpu_memory(self):
        return self._gpu_memory

    @gpu_memory.setter
    def gpu_memory(self, gpu_memory):
        self._gpu_memory = gpu_memory

    @property
    def gpu_vrm_core(self):
        return self._gpu_vrm_core

    @gpu_vrm_core.setter
    def gpu_vrm_core(self, gpu_vrm_core):
        self._gpu_vrm_core = gpu_vrm_core

    @property
    def gpu_hot_spot(self):
        return self._gpu_hot_spot

    @gpu_hot_spot.setter
    def gpu_hot_spot(self, gpu_hot_spot):
        self._gpu_hot_spot = gpu_hot_spot

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        self._created_at = created_at

    @property
    def pc_id(self):
        return self._pc_id

    @pc_id.setter
    def pc_id(self, pc_id):
        self._pc_id = pc_id
