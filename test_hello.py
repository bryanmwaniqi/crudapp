import unittest
from hello import add


class TestFormulas(unittest.TestCase):
	def test_add(self):
		self.assertEqual(add(3, 4), 9)