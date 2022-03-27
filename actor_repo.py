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
    def test_addActor(self):
        """Actors can be added to their repository"""
        repo = ActorStore()
        name = 'George Washington'
        year_of_birth = 1940
        year_of_death = 1976
        yearsActive = range(year_of_birth, year_of_death)
        self.assertEqual(repo.addActor(name, yearsActive), (name, yearsActive))

    def test_next(self):
        """Get the next actor in the repository sorted by year_of_birth descand loops back to the top when the list is exhausted"""
        repo = ActorStore()
        name1 = 'George'
        name2 = 'George'
        years_active1 = range(1940, 1941)
        years_active2 = range(1930, 1931)
        repo.addActor(name2, years_active2)
        repo.addActor(name1, years_active1)
        self.assertEqual(repo.next(), (name1, years_active1))
        self.assertEqual(repo.next(), (name2, years_active2))
        self.assertEqual(repo.next(), (name1, years_active1))
        
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

class ActorStore():
    """The Actor specialized repository"""
    def __init__(self):
        self._repo = []
        self._last = -1

    def addActor(self, name, yearsActive):
       """Add an actor to the repository"""
       assert len(yearsActive) > 0, "actors must be born before they die"
       self._repo.append((name, yearsActive))
       self._repo.sort(key=lambda a: min(a[1]), reverse=True)
       return name, yearsActive

    def next(self):
        """get the next actor in the timeline"""
        self._last += 1
        self._last %= len(self._repo)
        return self._repo[self._last]
