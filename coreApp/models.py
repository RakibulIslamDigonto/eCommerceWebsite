from django.db import models

# Create your models here.
class BaseModel(models.Model):
    create_at = models.DateField(auto_now_add=True, null=True)
    modified_at = models.DateField(auto_now=True, null=True)
    enable = models.BooleanField(default=True)
    class Meta:
        abstract = True


