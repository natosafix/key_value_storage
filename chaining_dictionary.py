class Entry:
    def __init__(self, hash_code=None, key=None, next_entry=None, value=None):
        self.hash_code = hash_code
        self.key = key
        self.next_entry = next_entry
        self.value = value

    def get_entries_chain(self, entries):
        current_entry = self
        while True:
            yield current_entry
            if current_entry.next_entry == -1:
                break
            current_entry = entries[current_entry.next_entry]


class ChainingDictionary:
    def __init__(self, capacity=3):
        self._buckets = [None] * capacity
        self._entries = [None] * capacity
        self._elements_count = 0

    def add(self, key, value):
        if self._elements_count == len(self._entries):  # расширение словаря
            self._extend()
        self._elements_count += 1

        new_entry = Entry(self._get_hash_code(key), key, -1, value)

        if self._buckets[new_entry.hash_code] is not None:
            new_entry.next_entry = self._buckets[new_entry.hash_code]
            for entry in self._entries[new_entry.next_entry].get_entries_chain(
                    self._entries):
                if new_entry.key == entry.key:
                    raise KeyError(
                        f'Key {new_entry.key} already in dictionary')

        self._entries[self._elements_count - 1] = new_entry
        self._buckets[new_entry.hash_code] = self._elements_count - 1

    def __getitem__(self, key):
        return self._find_entry(key).value

    def __setitem__(self, key, value):
        try:
            entry = self._find_entry(key)
            entry.value = value
        except KeyError:
            self.add(key, value)


    def _find_entry(self, key):
        key_hash_code = self._get_hash_code(key)
        entry_index = self._buckets[key_hash_code]
        if entry_index is None:
            raise KeyError(f'No key {key} in dictionary')

        first_entry = self._entries[entry_index]
        for entry in first_entry.get_entries_chain(self._entries):
            if entry.key == key:
                return entry
        raise KeyError(f'No key {key} in dictionary')

    def items(self):
        for i in range(self._elements_count):
            entry = self._entries[i]
            yield entry.key, entry.value

    def keys(self):
        for i in range(self._elements_count):
            entry = self._entries[i]
            yield entry.key

    def values(self):
        for i in range(self._elements_count):
            entry = self._entries[i]
            yield entry.value
    def __str__(self):
        parsed_entries = []
        for key, value in self.items():
            parsed_entries.append(
                f'{key.__str__()}: {value.__str__()}')
        return f'{{{", ".join(parsed_entries)}}}'

    def __len__(self):
        return self._elements_count

    def _extend(self):
        new_capacity = self._find_next_prime(len(self._entries) * 2)
        entries = []
        for key, value in self.items():
            entries.append((key, value))
        self.__init__(new_capacity)
        for key, value in entries:
            self.add(key, value)

    def _get_hash_code(self, key):
        try:
            key_hash_code = hash(key) % len(self._entries)
        except TypeError:
            raise
        return key_hash_code

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
