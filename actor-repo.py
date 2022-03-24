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
        self.assertEqual(StoreTest.repo._complete, False)
        self.assertEqual(StoreTest.repo.complete(), StoreTest.repo)
        self.assertEqual(StoreTest.repo._complete, True)
    def test_close(self):
        pass

class Store():
    def __init__(self):
        self._complete = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return self

    def complete(self):
        self._complete = True
        return self
# Create

# Read

# Update

# Delete
