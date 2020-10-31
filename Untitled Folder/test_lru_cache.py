from sample import lru_cache
import pytest

@pytest.fixture()
def test_cache():
    cache = lru_cache(2)
    cache.put(1,2)
    return cache

class Testlru_Cache:

    def test_put_get(self, test_cache):
        test_cache.put(2,4)
        assert test_cache.get(2) == 4

    def test_delete(self, test_cache):
        test_cache.delete(1)
        assert test_cache.get(1) is -1

    def test_reset(self, test_cache):
        test_cache.reset()
        assert test_cache.get(1) is -1



