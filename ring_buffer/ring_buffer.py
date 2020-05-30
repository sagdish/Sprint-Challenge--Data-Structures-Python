class RingBuffer:
    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.pointer = 0
        self.capacity = capacity

    def append(self, item):
        self.storage[self.pointer] = item
        self.pointer += 1
        # print('capacity and pointer' , self.capacity, self.pointer)

        if self.pointer > self.capacity -1:
            self.pointer = 0
            # print('pointer', self.pointer)

    def get(self):
        current = [item for item in self.storage if item is not None]
        # print('current', current)
        return current
        