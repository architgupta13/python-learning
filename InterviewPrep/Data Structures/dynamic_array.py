class DynamicArray:

    def __init__(self, capacity: int):
        self.arr = [None] * capacity
        self.capacity = capacity
        self.current_size = 0

    def get(self, i: int) -> int:
        if i >= self.capacity:
            raise ArrayOutOfBoundsException

        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if i >= self.capacity:
            raise ArrayOutOfBoundsException

        if self.arr[i] is None:
            self.current_size += 1

        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.current_size + 1 == self.capacity:
            raise ArrayOutOfBoundsException

        self.arr[self.current_size + 1] = n
        self.current_size += 1

    def popback(self) -> int:
        if self.current_size == 0:
            return None

        val = self.arr[self.current_size]
        self.arr[self.current_size] = None
        self.current_size -= 1
        return val

    def resize(self) -> None:
        extension = [None] * self.capacity
        self.arr.extend(extension)
        self.capacity *= 2

    def getSize(self) -> int:
        return self.current_size

    def getCapacity(self) -> int:
        return self.capacity
