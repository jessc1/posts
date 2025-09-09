from django.db import models
from abstract.models import AbstractModel

class Comment(AbstractModel):
    post = models.ForeignKey("post.Post", on_delete=models.CASCADE)
    author = models.ForeignKey("user.User", on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.author.full_name