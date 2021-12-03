from django.db import models

# Create your models here.
class Driver(models.Model):
    driver = models.CharField(max_length=25, null=True)

    def __str__(self):
        return self.driver
