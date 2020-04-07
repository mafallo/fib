#fibonnacci
#La suite de Fibonacci est une suite d'entiers dans laquelle chaque terme est la somme des deux termes qui le précèdent. 
#Elle commence généralement par les termes 0 et 1 (parfois 1 et 1) et ses premiers termes sont :
# 0 => 0, 
# 1 => 1, 
# 2 => 1, 
# 3 => 2, 
# 4 => 3, 
# 5 => 5, 
# 6 => 8, 
# 7 => 13, 
# 8 => 21
import unittest
import fibonacci

class TestFibo(unittest.TestCase):
	def test_donothing(self):
		result = True
		self.assertEqual(result, True)

	def test_shouldreturn0ifNequal0(self):
		result = fibonacci.fibonacci(0)
		self.assertEqual(result,0)
	
	def test_shouldreturn1ifNequal1(self):
		result = fibonacci.fibonacci(1)
		self.assertEqual(result,1)

	def test_shouldreturn1ifNequal2(self):
		result = fibonacci.fibonacci(2)
		self.assertEqual(result,1)

	def test_shouldreturn2ifNequal3(self):
		result = fibonacci.fibonacci(3)
		self.assertEqual(result,2)

	def test_shouldreturn3ifNequal4(self):
		result = fibonacci.fibonacci(4)
		self.assertEqual(result,3)

	def test_shouldreturn5ifNequal5(self):
		result = fibonacci.fibonacci(5)
		self.assertEqual(result,5)

	def test_shouldreturn8ifNequal6(self):
		result = fibonacci.fibonacci(6)
		self.assertEqual(result,8)

	def test_shouldreturn13ifNequal7(self):
		result = fibonacci.fibonacci(7)
		self.assertEqual(result,13)

	def test_shouldreturn21ifNequal8(self):
		result = fibonacci.fibonacci(8)
		self.assertEqual(result,21)

	def test_shouldReturn1IfNbrIsminus1(self):
		result = fibonacci.fibonacci(-1)
		self.assertEqual(result, 1)

	def test_shouldRetunrminus1IfNbrIsminus2(self):
		result = fibonacci.fibonacci(-2)
		self.assertEqual(result, -1)

	def test_shouldRetun2IfNbrIsminus3(self):
		result = fibonacci.fibonacci(-3)
		self.assertEqual(result, 2)

	def test_shouldRetunrminus3IfNbrIsminus4(self):
		result = fibonacci.fibonacci(-4)
		self.assertEqual(result, -3)

if __name__ == '__main__':
	unittest.main()
