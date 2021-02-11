from django.db import models
from django.contrib.postgres.fields import JSONField


class Storage(models.Model):
    name = JSONField()
