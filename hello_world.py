# import unittest
# from city_functions import city

# class CityTestCase(unittest.TestCase):

# 	def test_city_country(self):
# 		city_name = city('santiago', 'chile')
# 		self.assertEqual(city_name, 'Santiago, Chile')

# 	def test_city_country_population(self):
# 		city_name = city('santiago', 'chile', '5000000')
# 		self.assertEqual(city_name, 'Santiago, Chile - population 5000000')

# unittest.main()

import unittest
from city_functions import Employee

class EmployeeTestCase(unittest.TestCase):

	def setUp(self):
		self.john = Employee('john', 'doe', 1000)

	def test_give_default_raise(self):
		self.john.give_raise()
		self.assertEqual(self.john.salary, 6000)

	def test_give_custom_raise(self):
		self.john.give_raise(2000)
		self.assertEqual(self.john.salary, 3000)

unittest.main()