import unittest
import sys
from linguine.ops.remove_caps import RemoveCapsGreedy, RemoveCapsPreserveNNP

class RemoveCapsTest(unittest.TestCase):

    def setUp(self):
        self.op = RemoveCapsGreedy()

    def test_run_greedy(self):
        self.op = RemoveCapsGreedy()
        self.test_data = '''Removes all non-proper-noun capitals from a given text. Removes capital letters from text, even for Bill Clinton. Accepts as input a non-tokenized string.'''
        self.assertEqual(self.op.run(self.test_data),
        '''removes all non-proper-noun capitals from a given text. removes capital letters from text, even for bill clinton. accepts as input a non-tokenized string.''')

    def test_run_preserve_nnp(self):
        self.op = RemoveCapsPreserveNNP()
        self.test_data = '''Removes all non-proper-noun capitals from a given text. Removes capital letters from text, even for Bill Clinton. Accepts as input a non-tokenized string.'''
        self.assertEqual(self.op.run(self.test_data),
        '''removes all non-proper-noun capitals from a given text. removes capital letters from text, even for Bill Clinton. accepts as input a non-tokenized string.''')

if __name__ == '__main__':
    unittest.main()
