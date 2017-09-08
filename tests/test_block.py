import unittest
import sys
sys.path.append('src')
from block import Block

class TestBlockTest(unittest.TestCase):

    def test_valid_index(self):
        prev_block = Block(index=0, previous_hash='0', timestamp=1, data='first block')
        block = Block(index=1, previous_hash='0', timestamp=1, data='second block')
        self.assertTrue(block.has_valid_index(prev_block))

    def test_invalid_index(self):
        prev_block = Block(0, '0', 1, 'first block')
        block = Block(2, '0', 1, 'second block')
        self.assertFalse(block.has_valid_index(prev_block))

    def test_valid_hash(self):
        block = Block(1, '0', '0', 'first block')
        self.assertTrue(block.has_valid_hash())

    def test_valid_previous_hash(self):
        prev_block = Block(index=0, previous_hash='0', timestamp=1, data='first block')
        block = Block(index=1, previous_hash=prev_block.hash, timestamp=1, data='second block')
        self.assertTrue(block.has_valid_previous_hash(prev_block))

    def test_invalid_previous_hash(self):
        prev_block = Block(index=0, previous_hash='0', timestamp=1, data='first block')
        block = Block(index=1, previous_hash='1', timestamp=1, data='second block')
        self.assertFalse(block.has_valid_previous_hash(prev_block))

if __name__ == '__main__':
    unittest.main()
