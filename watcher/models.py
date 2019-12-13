from django.db import models
from datetime import (
     datetime,
     timezone
)

class Push(models.Model):
    who = models.CharField(null=True)
    when = models.DateTimeField(null=False) # default to datetime.now(timezone.utc)
    where = models.CharField(null=False)
    templates = models.CharField(null=False)
    locations = models.CharField(null=False)
