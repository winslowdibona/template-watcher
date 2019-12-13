from django.db import models
from datetime import (
     datetime,
     timezone
)

class Push(models.Model):
    who = models.CharField(max_length=255, null=True)
    when = models.DateTimeField(null=False) # default to datetime.now(timezone.utc)
    where = models.CharField(max_length=255, null=False)
    templates = models.TextField()
    locations = models.TextField()
