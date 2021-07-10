from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'images',default='SOME IMAGE')
    bio = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')


class Image(models.Model):
    image = models.ImageField(upload_to = 'images/',default='SOME IMAGE')
    image_name = models.CharField(max_length=50)
    image_caption = models.CharField(max_length=200)
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    likes = models.ManyToManyField(User, related_name='likes', blank=True, )
    date = models.DateTimeField(auto_now_add = True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()


class Comments(models.Model):
    comments = models.CharField(max_length=200)
