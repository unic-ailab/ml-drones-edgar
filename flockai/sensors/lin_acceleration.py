from flockai.interfaces.sensor import ISensor


class LinearAccelerationSensor(ISensor):

    def __init__(self, file):
        super().__init__(file)
        self.cum_sum = 0
        self.entries = 0

    def get_values(self):
        data = self._get_data()
        lin_acceleration = float(data)
        self.entries += 1
        self.cum_sum += lin_acceleration
        lin_acceleration_avg = self.cum_sum / self.entries


        return lin_acceleration_avg