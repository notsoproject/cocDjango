from django.db import models
from djongo import models as djongo_models
from bson import ObjectId

# Create your models here.

class Progress(models.Model):
    id = djongo_models.ObjectIdField()

    def __str__(self):
        return f'{self.id}-Progress'