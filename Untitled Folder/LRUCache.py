from collections import OrderedDict

class LRUCache:

    # initialising capacity
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)

    def delete(self, key: int):
        if key in self.cache:
            del self.cache[key]
        else:
            return None

    def reset(self):
        self.__init__(self.capacity)


cache = LRUCache(2)


cache.put(1, 11)
print(cache.cache)
cache.put(2, 22)
print(cache.cache)
cache.get(1)
print(cache.cache)
cache.put(3, 33)
print(cache.cache)
cache.get(2)
print(cache.cache)
cache.put(4, 44)
print(cache.cache)
cache.get(1)
print(cache.cache)
cache.get(3)
print(cache.cache)
cache.get(4)
print(cache.cache)
cache.reset()
print(cache.cache)

