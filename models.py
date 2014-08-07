from django.db import models
from datetime import datetime


class Page(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = datetime.today()
        self.updated_at = datetime.today()
        return super(Page, self).save(*args, **kwargs)
