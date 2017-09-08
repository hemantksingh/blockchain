import hashlib

class Block(object):
    def __init__(self, index, previous_hash, timestamp, data):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calc_hash()

    def __str__(self):
        return str(self.index) + self.previous_hash + str(self.timestamp) + self.data

    def has_valid_index(self, prev_block):
         return self.index == prev_block.index + 1

    def has_valid_hash(self):
        return self.hash == self.calc_hash()

    def has_valid_previous_hash(self, prev_block):
        return self.previous_hash == prev_block.hash

    def calc_hash(self):
        return hashlib.sha256(str(self).encode()).hexdigest()
