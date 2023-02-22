class HashMap:
    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def __repr__(self):
        buckets = []
        for v in self.hashmap:
            if v != None:
                buckets.append(v)
        return str(buckets)

        # Hash Function
    def key_to_index(self, key):
        ascii_values = list(key.encode('ascii'))
        return sum(ascii_values) % len(self.hashmap)

    def insert(self, key, value):
        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    def get(self, key):
        index = self.key_to_index(key)
        if self.hashmap[index]:
            return self.hashmap[index][1]
        raise Exception("sorry, key not found")
