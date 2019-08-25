from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

# Profile contains the additional user information
# such as bio and contact information
class Profile(models.Model):
    '''
    For maintaining user profile information
    '''
    website = models.URLField(null=True)
    bio = models.TextField(null=True)
    address = models.TextField(null=True)
    phone_no = models.CharField(max_length=12, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)

    profile_pic = models.ImageField(upload_to="user/", default="default_user_profile.jpg")

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return self.user.username+" profile"

    def get_absolute_url(self):
        return reverse("account:user-profile", kwargs={"pk": self.pk})

# Here we have declared a signal
# when User is created, it sends a signal, 
# and a new profile is created for that new user
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance,first_name=instance.first_name,last_name=instance.last_name,email=instance.email)