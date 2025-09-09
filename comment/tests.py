import pytest
from comment.models import Comment 
from fixtures.user import user
from fixtures.post import post

@pytest.mark.django_db
def test_create_comment(user, post):
    comment = Comment.objects.create(author=user,post=post, body="example comment")
    assert comment.author == user
    assert comment.post == post
    assert comment.body == "example comment"

