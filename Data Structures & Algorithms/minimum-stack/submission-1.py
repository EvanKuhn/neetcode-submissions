class MinStack:

    def __init__(self):
        self._values = []
        self._mins = []

    def push(self, val: int) -> None:
        new_min = val if not self._mins else min(val, self._mins[-1])
        self._values.append(val)
        self._mins.append(new_min)

    def pop(self) -> None:
        self._values.pop()
        self._mins.pop()

    def top(self) -> int:
        return self._values[-1]

    def getMin(self) -> int:
        return self._mins[-1]
        
