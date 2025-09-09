import pytest
from user.models import User

test_user = {
    "username" : "ieie",
    "email": "ieie@email.com",
    "password": "ieiepwd",
}

test_superuser = {
    "username": "user_superuser",
    "email": "superuser@email.com",
    "password": "superuserpwd",
}


@pytest.mark.django_db
def test_creating_user():
    user = User.objects.create_user(**test_user)
    assert user.username == test_user["username"]
    assert user.email == test_user["email"]


@pytest.mark.django_db
def test_creating_superuser():
    superuser = User.objects.create_superuser(**test_superuser)
    assert superuser.username == test_superuser["username"]
    assert superuser.email == test_superuser["email"]
    assert superuser.is_superuser == True
    assert superuser.is_staff == True


    