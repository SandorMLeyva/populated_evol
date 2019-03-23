import heapq

class Heap:
    def __init__(self):
        self.data = []

    def insert(self, item):
        heapq.heappush(self.data, item)
        # self.data.append(item)
        # self.data.sort(key= lambda x: x.time)

    def ext_min(self):
        return heapq.heappop(self.data)
        # return self.data.pop(0)

    def is_empty(self):
        return len(self.data) == 0
