from django.db import models
from abstract.models import AbstractModel
from user.models import User
class Post(AbstractModel):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title =  models.CharField(max_length=255)
    content =  models.CharField(max_length=255)

    def __str__(self):
        return f"{self.author.username}"
    
    class Meta:
        db_table = "post"