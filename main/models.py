from django.db import models
import uuid

# Create your models here.
class VBucksEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    bonus = models.IntegerField()