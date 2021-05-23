from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse


class Profile(models.Model):
    """
    A User profile containing additional data
    """
    bio = models.TextField(null=True, help_text="Few words about yourself.")
    website = models.URLField(null=True, help_text="Link to your online website.")

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    def __str__(self):
        return f"{self.user.username} profile"
    
    def get_absolute_url(self):
        return reverse("account:profile-detail", kwargs={"pk":self.pk})


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
