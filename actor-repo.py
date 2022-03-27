import unittest

class StoreTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.repo = Store()

    def test_enter(self):
        """test that __enter__ is available for context managers"""
        self.assertEqual(StoreTest.repo.__enter__(), StoreTest.repo)
    def test_exit(self):
        """test that __exit__ is available for context managers"""
        self.assertEqual(StoreTest.repo.__exit__(None, None, None), StoreTest.repo)
    def test_complete(self):
        """test that complete can be used to control transaction status"""
        self.assertEqual(StoreTest.repo._complete, False)
        self.assertEqual(StoreTest.repo.complete(), StoreTest.repo)
        self.assertEqual(StoreTest.repo._complete, True)
    def test_close(self):
        pass

class ActorStoreTest(unittest.TestCase):
    """The persistence manager for actors."""
    @classmethod
    def setUpClass(cls):
        cls.repo = ActorStore()

    def test_addActor(self):
        """Actors can be added to their repository"""
        name = 'George Washington'
        year_of_birth = 1940
        year_of_death = 1976
        yearsActive = range(year_of_birth, year_of_death)
        self.assertEqual(ActorStoreTest.repo.addActor(name, yearsActive), (name, yearsActive))

        
class Store():
    """The base type of all repositories. Intended to provide a seperation between reading data-models and handling persistence. Transactions are marked as complete by calling 'complete'"""
    def __init__(self):
        self._complete = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return self

    def complete(self):
        self._complete = True
        return self
# Read

# Update

# Delete
