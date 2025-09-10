from rest_framework import status
from fixtures.user import user
from configtest import client

class TestUserViewSet:
    endpoint ='/api/users/'

    def test_list(self, client, user):
        client.force_authenticate(user=user)
        response = client.get(self.endpoint)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 1
    
    def test_retrieve(self, client, user):
        client.force_authenticate(user=user)
        response = client.get(self.endpoint + str(user.id) + "/")
        assert response.data['id'] == user.id
        assert response.data['username'] == user.username
        assert response.data["email"] == user.email