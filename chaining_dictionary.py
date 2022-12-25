class Entry:
    def __init__(self, hash_code=None, key=None, next_entry=None, value=None):
        self.hash_code = hash_code
        self.key = key
        self.next_entry = next_entry
        self.value = value

    def get_next_entries(self, entries):
        current_entry = entries[self.next_entry]
        while True:
            if current_entry == -1 or current_entry is None:
                break
            yield current_entry
            current_entry = entries[current_entry.next_entry]


class ChainingDictionary:
    def __init__(self, capacity=3):
        self.buckets = [None] * capacity
        self.entries = [None] * capacity
        self.elements_count = 0

    def __add__(self, key, value):
        self.elements_count += 1
        if self.elements_count > len(self.entries):  # расширение словаря
            self._extend()
            self.elements_count += 1
        try:
            new_entry = Entry(hash(key) % len(self.entries), key, -1, value)
        except TypeError:
            raise
        if self.buckets[new_entry.hash_code] is not None:
            new_entry.next_entry = self.buckets[new_entry.hash_code]
        for entry in new_entry.get_next_entries(self.entries):
            if new_entry.key == entry.key:
                raise KeyError(f'Key {new_entry.key} already in dictionary')
        self.entries[self.elements_count - 1] = new_entry
        self.buckets[new_entry.hash_code] = self.elements_count - 1

    def items(self):
        for entry in self.entries:
            if entry is not None:
                yield entry.key, entry.value

    def _extend(self):
        new_capacity = self._find_next_prime(len(self.entries) * 2)
        entries = []
        for key, value in self.items():
            entries.append((key, value))
        self.__init__(new_capacity)
        for key, value in entries:
            self.__add__(key, value)

    @staticmethod
    def _find_next_prime(start):
        current = start + 1
        while True:
            is_prime = True
            for i in range(2, round(current ** 0.5)):
                if current % i == 0:
                    is_prime = False
                    break
            if is_prime:
                return current
            current += 1
