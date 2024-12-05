import maiapy
import unittest

class TestHello(unittest.TestCase):

  def test_hello(self):
    self.assertIsInstance(maiapy.hello(), str)
