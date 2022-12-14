class HashTable:
    def __init__(self, size: int):
        self.index = 0
        self.items = [[] for _ in range(size)]
        self.size = size

    def hash(self, key) -> int:
        key_type = type(key).__name__
        if key_type == "int":
            return key % self.size
        elif key_type == "str":
            sum = 0
            for character in key:
                sum += ord(character) - ord('0')
            return sum % self.size

    def get_position(self, key):
        for item in self.items[self.hash(key)]:
            if item[0] == key:
                return item[1]
        return -1

    def insert(self, key):
        if self.contains(key):
            return self.get_position(key)
        self.items[self.hash(key)].append((key, self.index))
        self.index += 1
        return self.get_position(key)

    def delete(self, key) -> None:
        position = self.hash(key)
        for el in self.items[position]:
            if el[0] == key:
                self.items[position].remove(el)

    def contains(self, key):
        for element in self.items[self.hash(key)]:
            if element[0] == key:
                return True
        return False

    def get_items(self):
        all_items = []
        for i in range(self.size):
            items = self.items[i]
            if len(items) != 0:
                for item in items:
                    all_items.append(item)
        return all_items

    def __str__(self) -> str:
        representation = ""
        for i in range(self.size):
            items = self.items[i]
            if len(items) != 0:
                for item in items:
                    representation += str(item) + "\n"
        return representation
