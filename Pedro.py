import unittest

def fun(x):

    return x == "Pedro"

class MyTest(unittest.TestCase):

    def test(self):
        self.assertTrue(fun("Sean"))

if __name__== '__main__':

    unittest.main()