class MeasurementIncrease():
    def __init__(self):
        # Read the input file
        with open("input.txt") as f:
            measurements = f.read().split("\n")
            # Try to remove the null index
            try:
                measurements.remove("")
            except ValueError as e:
                pass
            self._measurements_list = []
            for key, measurement in enumerate(measurements):
                try:
                    self._measurements_list.append([
                        int(measurements[key]), int(measurements[key+1]), int(measurements[key+2])])
                except IndexError as e:
                    pass
        self._count = 0

    def start(self):
        result = self._calculate()
        print(result)

    def _calculate(self):
        count = 0
        for key, measurment in enumerate(self._measurements_list):
            if(sum(measurment) > sum(self._measurements_list[key - 1])):
                count += 1
        return count
