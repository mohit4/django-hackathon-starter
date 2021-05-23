from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class TimeStampedModel(models.Model):
    """
    Abstract model class with ``created`` and ``updated`` time stamps
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Object(TimeStampedModel):
    """
    Object model with all model fields
    """

    CATEGORY_CHOICES = (
        ( 'RND', 'Research & Development' ),
        ( 'AUT', 'Automobile' ),
        ( 'INF', 'Infrastructure' ),
    )

    title = models.CharField(max_length=50, help_text="Title of the object")
    description = models.TextField(null=True, blank=True, help_text="Few words about the object")

    credits = models.PositiveIntegerField(null=True, blank=True, help_text="Credits earned by object.")
    value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="Value of one unit of object.")
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES, null=True, blank=True, help_text="Category for the Object.")

    weblink = models.URLField(max_length=200, null=True, blank=True, help_text="Online link for the Object.")

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="objects")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("app:object-detail", kwargs={"pk": self.pk})
