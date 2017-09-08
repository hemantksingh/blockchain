import unittest
import sys
sys.path.append('src')
from block import Block
from blockchain import BlockChain

class BlockBuilder(object):
    def __init__(self):
        self._index=0
        self._previous_hash='0'
        self._data='first block'

    def index(self, index):
        self._index=index
        return self

    def previous_hash(self, previous_hash):
        self._previous_hash = previous_hash
        return self

    def data(self, data):
        self._data=data
        return self

    def build(self):
        return Block(
            index=self._index,
            previous_hash=self._previous_hash,
            data=self._data
        )

class TestBlockTest(unittest.TestCase):

    def test_valid_index(self):
        prev_block = BlockBuilder().index(0).build()
        block = BlockBuilder().index(1).build()
        self.assertTrue(block.has_valid_index(prev_block))

    def test_invalid_index(self):
        prev_block = BlockBuilder().index(0).build()
        block = BlockBuilder().index(2).build()
        self.assertFalse(block.has_valid_index(prev_block))

    def test_valid_hash(self):
        block = BlockBuilder().build()
        self.assertTrue(block.has_valid_hash())

    def test_valid_previous_hash(self):
        prev_block = BlockBuilder().build()
        block = BlockBuilder().previous_hash(prev_block.hash).build()
        self.assertTrue(block.has_valid_previous_hash(prev_block))

    def test_invalid_previous_hash(self):
        prev_block = BlockBuilder().build()
        block = BlockBuilder().previous_hash('invalid').build()
        self.assertFalse(block.has_valid_previous_hash(prev_block))

class TestBlockChain(unittest.TestCase):

    def test_initialise_blockchain(self):
        blockchain = BlockChain()
        block = blockchain.latest_block()

        self.assertEqual(1, blockchain.size())
        self.assertEqual('first block', block.data)

    def test_generate_next_block(self):
        data = 'this is the new block'
        blockchain = BlockChain()
        blockchain.generate_next_block(data)

        self.assertEqual(data, blockchain.latest_block().data)
        self.assertEqual(2, blockchain.size())

    def test_adding_valid_new_block(self):
        blockchain = BlockChain()
        prev_block = blockchain.latest_block()
        new_block = Block(
            index=prev_block.index+1,
            previous_hash=prev_block.hash,
            data='second block')
        blockchain.add_block(new_block)

        self.assertEqual('second block', blockchain.latest_block().data)
        self.assertEqual(2, blockchain.size())

    def test_new_block_with_invalid_index_not_added(self):
        blockchain = BlockChain()
        prev_block = blockchain.latest_block()
        new_block = Block(
            index=3,
            previous_hash=prev_block.hash,
            data='second block')
        blockchain.add_block(new_block)

        self.assertEqual(1, blockchain.size())
        self.assertNotEqual('second block', blockchain.latest_block().data)

    def test_new_block_with_invalid_previous_hash_not_added(self):
        blockchain = BlockChain()
        prev_block = blockchain.latest_block()
        new_block = Block(
            index=prev_block.index+1,
            previous_hash='0',
            data='second block')
        blockchain.add_block(new_block)

        self.assertEqual(1, blockchain.size())
        self.assertNotEqual('second block', blockchain.latest_block().data)

    def test_new_block_with_invalid_hash_not_added(self):
        blockchain = BlockChain()
        prev_block = blockchain.latest_block()
        new_block = Block(
            index=prev_block.index+1,
            previous_hash=prev_block.hash,
            data='second block')
        new_block.hash = 'crap'
        blockchain.add_block(new_block)

        self.assertEqual(1, blockchain.size())
        self.assertNotEqual('second block', blockchain.latest_block().data)

if __name__ == '__main__':
    unittest.main()
