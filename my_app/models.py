from django.db import models
from django.contrib.auth.models import User


# MODELING AUTHORS DATABASE
class Author(models.Model):
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField(
        upload_to='authors/', blank=True, null=True)
    bio = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

# MODELING EDITIONS


class Edition(models.Model):
    title = models.CharField(max_length=200)
    number = models.IntegerField()
    thumb = models.ImageField(upload_to='editions/', blank=True, null=True)
    date = models.DateField(auto_now=True, editable=False)

    def __str__(self):
        return f"{self.title} - No. {self.number}"

    class Meta:
        verbose_name = 'Edition'
        verbose_name_plural = 'Editions'

# MODELING STORIES


class Story(models.Model):
    edition = models.ForeignKey(
        Edition, on_delete=models.CASCADE, related_name="stories")
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=10000)
    date = models.DateField(auto_now=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'
