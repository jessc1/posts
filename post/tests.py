import pytest
from fixtures.user import user 
from post.models import Post

@pytest.mark.django_db
def test_create_post(user):
    post = Post.objects.create(author=user,title="Example Title", content="Example Content")
    assert post.title == "Example Title"
    assert post.content == "Example Content"
    assert post.author == user
