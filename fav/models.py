from django.db import models
from django.contrib.auth.models import User

class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal_id = models.CharField(max_length=50)
    name = models.CharField(max_length=200, default="Unknown Meal")
    image_url = models.URLField(default="")
    category = models.CharField(max_length=100, default="General")
    cuisine = models.CharField(max_length=100, default="Unknown")
    youtube_url = models.URLField(default="", blank=True)
    source_url = models.URLField(default="", blank=True)

    def __str__(self):
        return self.name