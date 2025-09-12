import pytest
from rest_framework import status
from fixtures.user import user
from fixtures.post import post
from configtest import client, clear_cache
from django.urls import reverse
from django.core.cache import cache

class TestPostViewSet:
    endpoint ='/api/posts/'

    def test_list(self, client, user, post):
        client.force_authenticate(user=user)
        response = client.get(self.endpoint)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 1
    
    def test_retrieve(self, client, user, post):
        client.force_authenticate(user=user)
        response = client.get(self.endpoint + str(post.id) + "/")
        assert response.data['id'] == post.id
        assert response.data['author'] == post.author.username
    
    def test_create(self, client, user):
        client.force_authenticate(user=user)
        data = {"author": user.username, "title": "test title", "content": "test content"}
        response = client.post(self.endpoint, data)
        assert response.status_code == status.HTTP_201_CREATED
    
    def test_patch(self, client, user, post):
        client.force_authenticate(user=user)
        data = {"title": "update title", "content": "update content"}
        response = client.patch(self.endpoint + str(post.id) + "/", data)
        assert response.data["title"] == data["title"]
        assert response.data["content"] == data["content"]
        assert response.status_code == status.HTTP_200_OK
        
    
    def test_delete(self, client, user, post):
        client.force_authenticate(user=user)
        response = client.delete(self.endpoint + str(post.id) + "/")
        assert response.data == {}
        assert response.status_code == status.HTTP_200_OK
    
    def test_list_anonymous(self, client, post):
        response = client.get(self.endpoint)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 1
    
    def test_retrieve_anonymous(self, client, post):
        response = client.get(self.endpoint + str(post.id) + "/")
        assert response.status_code == status.HTTP_200_OK
    
    def test_create_anonymous(self, client):
        data = {"author": "user", "title": "example title", "content": "example content"}
        response = client.post(self.endpoint, data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_patch_anonymous(self, client, post):
        data = {"title": "update title", "content": "update content"}
        response = client.put(self.endpoint + str(post.id) + "/", data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_delete_anonymous(self, client, post):
        response = client.delete(self.endpoint + str(post.id) + "/")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @pytest.mark.django_db
    def test_cached_posts(self, client, clear_cache, post):
        response = client.get(self.endpoint)
        assert response.status_code == 200

        response1 = client.get(self.endpoint)
        assert response1.status_code == 200
        



        
