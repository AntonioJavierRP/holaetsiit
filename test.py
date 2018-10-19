import unittest
import server

class TestMyServer(unittest.TestCase):

	def test_first(self):
		response = server.hello()
		self.assertIn("Hello", response)

if __name__ == '__main__':
	unittest.main()