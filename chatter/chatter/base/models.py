from django.conf import settings
from django.db import models


# Create your models here.
class Chat(models.Model):
    """A single chat from a User.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.CharField(max_length=200)
    created = models.DateTimeField(auto_add_now=True)
