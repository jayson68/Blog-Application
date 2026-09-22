from django.db import models
from django.contrib.auth.models import User




class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    profile_image = models.ImageField(
        upload_to="profile/",
        blank=True
    )

    bio = models.TextField(
        blank=True
    )


    def __str__(self):
        return self.user.username



class Post(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    
    
    title = models.CharField(
        max_length=200
    )

    content = models.TextField()

    image = models.ImageField(
        upload_to="posts/",
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.title