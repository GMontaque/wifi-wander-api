from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    memorable_word = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='images/', default='default_profile_q35ywj')
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_joined']

    def __str__(self):
        return f"{self.user.username}'s Profile"

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_profile, sender=User)
