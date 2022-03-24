import unittest

class StoreTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.repo = Store()

    def test_enter(self):
        self.assertEquals(StoreTest.repo.__enter__(), StoreTest.repo)
    def test_exit(self):
        pass
    def test_complete(self):
        pass
    def test_close(self):
        pass

class Store():
    def __init__(self):
        self.storage = []
# Create

# Read

# Update

# Delete
