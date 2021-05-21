from django.db import models


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
    title = models.CharField(max_length=50, help_text="Title of the object")
    description = models.TextField(null=True, blank=True, help_text="Few words about the object")

    def __str__(self):
        return self.title
