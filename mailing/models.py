from datetime import datetime
from django.db import models


class ContactData(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()

    def __str__(self):
        return self.email
