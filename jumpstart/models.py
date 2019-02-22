from django.db import models


class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='media', blank=True)

    def __str__(self):
        return self.profile_pic.path