from flockai.interfaces.sensor import ISensor


class VelocitySensor(ISensor):

    def __init__(self, file):
        super().__init__(file)
        self.cum_sum = 0
        self.entries = 0

    def get_values(self):
        data = self._get_data()
        velocity = float(data)
        self.entries += 1
        self.cum_sum += velocity
        velocity_avg = self.cum_sum / self.entries


        return velocity_avg