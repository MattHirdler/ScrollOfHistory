import unittest

class StoreTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.repo = Store()

    def test_enter(self):
        self.assertEquals(StoreTest.repo.__enter__(), StoreTest.repo)
    def test_exit(self):
        self.assertEqual(StoreTest.repo.__exit__(None, None, None), StoreTest.repo)
    def test_complete(self):
        pass
    def test_close(self):
        pass

class Store():
    def __init__(self):
        self.storage = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return self
# Create

# Read

# Update

# Delete
