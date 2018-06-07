# python3 -m unittest 1.py
# python3 -m pdb 1.py
	'''
	    ll   - list lines (show code)
		n    - next line
		s    - step into (into function)
		b 10 - breakpoint at the 10 line (stop at this line)
		c    - continue execution
	'''

import unittest
class TestPython(unittest.TestCase):
	def test_float_to_int_coercion(self):
		self.assertEqual(1, int(1.0))
	def test_get_empty_dict(self):
		self.assertIsNone({}.get('key'))
	def test_trueness(self):
		self.assertTrue(bool(10))

'''

...

Ran 3 tests in 0.000s

OK
'''
