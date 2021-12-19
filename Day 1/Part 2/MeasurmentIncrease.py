class MeasurementIncrease():
    def __init__(self):
        # Read the input file
        with open("input.txt") as f:
            self.measurements = f.read().split("\n")
            # Try to remove the null index
            try:
                self.measurements.remove("")
            except ValueError as e:
                pass
        self._count = 0

    def start(self):
        self._countmeasurements()
        print(self._count)

    def _countmeasurements(self):
        # Iterating over the measurements
        for index, item in enumerate(self.measurements):
            if(int(item) > int(self.measurements[index - 1])):
                self._count += 1
