from django.db import models

# Create your models here.
class Post(models.Model):

    athor = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    body = models.TextField()

    def __str__(self) -> str:
        return self.athor + ',' + self.title

# one to one 
class Addition(models.Model):

    image = models.URLField()
    styling = models.CharField(max_length=250)
    post = models.OneToOneField(Post,on_delete=models.CASCADE, related_name='addition')

    def __str__(self) -> str:
        return self.post.title


class Category(models.Model):

    name = models.CharField(max_length=50)
    post = models.ManyToManyField(Post,related_name='categories')

    def __str__(self) -> str:
        return self.name
