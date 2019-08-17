from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse

# Create your models here.
class Entity(models.Model):
    """
    This is a demo object containing all the basic fields
    """

    CAT_CHOICES = (
        ('AUT', 'Automobile'),
        ('INF', 'Infrastructure'),
        ('RND', 'Research and Development')
    )

    title = models.CharField(max_length=500)
    description = models.TextField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    points = models.PositiveIntegerField(default=10)
    cost = models.DecimalField(max_digits=12,decimal_places=2,default=99.99)
    category = models.CharField(max_length=3, choices=CAT_CHOICES)
    active = models.BooleanField(default=False)
    email = models.EmailField(max_length=100)

    profile_image = models.ImageField(upload_to="entity/", default="default_profile.jpg")
    cover_image = models.ImageField(upload_to="entity/", default="default_cover.jpg")

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)+"#"+self.title[:10]+"..."
    
    def get_absolute_url(self):
        return reverse("app:entity-detail", kwargs={"pk": self.pk})

class Comment(models.Model):
    """
    Comment object on an Entity
    """
    title = models.TextField(max_length=500)

    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)+"#"+str(self.user.id)+"#"+str(self.entity.id)