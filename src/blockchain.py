import time
from block import Block

class BlockChain(object):

    def __init__(self):
        initial_block = Block(
                index=0,
                previous_hash='0',
                timestamp=1495851743,
                data='first block'
            )
        self.store = [initial_block]

    def generate_next_block(self, data):
        new_block = Block(
                index=len(self.store),
                previous_hash=self.latest_block().hash,
                timestamp=int(time.time()),
                data=data
            )
        self.store.append(new_block)

    def latest_block(self):
        return self.store[-1]

    def size(self):
        return len(self.store)
