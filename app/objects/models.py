from django.db import models
from django.contrib.auth.models import User


class TimeStampedModel(models.Model):
    """
    Abstract model with ``created`` and ``modified`` time-stamps
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Object(TimeStampedModel):
    """
    An Object is a collection of all types of Django Fields
    """

    CATEGORY_CHOICES = (
        ('AUT', 'Automobiles'),
        ('INF', 'Infrastructure'),
        ('RND', 'Research and Development'),
    )

    title = models.CharField(
        max_length=100,
        primary_key=True,
        help_text="A unique text that identifies the object"
    )
    
    description = models.TextField(
        null=True,
        blank=True,
        help_text="Few words about the object"
    )

    category = models.CharField(
        max_length=3,
        choices=CATEGORY_CHOICES
    )

    credits = models.PositiveIntegerField(default=10)
    active = models.BooleanField(default=False)
    cost = models.DecimalField(max_digits=12, decimal_places=2, default=0.99)
    email = models.EmailField(max_length=50, null=True, blank=True)

    # image = models.ImageField(upload_to="object_images/", default="no_image.jpg")

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="objects")

    def __str__(self):
        return f"{self.title}"
