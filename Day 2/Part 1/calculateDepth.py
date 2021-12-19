
class CalculateDepth:
    def __init__(self):
        self._horizontal_position = 0
        self._depth = 0
        with open("input.txt") as f:
            self._inputs = f.read().split("\n")
            try:
                self._inputs.remove("")
            except ValueError as e:
                pass

    def start(self):
        print(self._calculate())

    def _calculate(self):
        self._horizontal_position = self._calculate_horizontal_position()
        self._depth = self._calculate_depth()
        return self._horizontal_position * self._depth

    def _calculate_horizontal_position(self):
        forward_count = 0
        for item in self._inputs:
            if("forward" in item):
                forward_count += int(item.split(" ")[1].strip())
        return forward_count

    def _calculate_depth(self):
        depth = 0
        for item in self._inputs:
            if "up" in item:
                depth -= int(item.split(" ")[1].strip())
            elif "down" in item:
                depth += int(item.split(" ")[1].strip())
        return depth


cd = CalculateDepth()
cd.start()
