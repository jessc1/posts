import pytest
from rest_framework.test import APIClient
from django.core.cache import cache

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture(autouse=True)
def clear_cache():
  cache.clear()
  yield
  cache.clear()
