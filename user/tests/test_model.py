import pytest
from user.models import User


@pytest.mark.django_db
def test_creating_user():
    user = User.objects.create_user(username="chengyi",email="chengyi@email.com", password="1234")
    assert user.username == "chengyi"
    assert user.email == "chengyi@email.com"

@pytest.mark.django_db
def test_creating_superuser():
    user = User.objects.create_superuser(username="chengyi",email="chengyi@email.com", password="1234")
    assert user.username == "chengyi"
    assert user.email == "chengyi@email.com"


    