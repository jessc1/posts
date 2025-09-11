import pytest
from user.models import User

test_user = {
    "username": "ieie",
    "email": "ieie@email.com",
    "password": "ieiepwd"
}

@pytest.fixture
def user(db) -> User:
    return User.objects.create_superuser(**test_user)