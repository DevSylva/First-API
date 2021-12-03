from django.db import models
from authentication.models import User
from driver.models import Driver

# Create your models here.
class Order(models.Model):

    STATUS = (
        ('PENDING', 'Pending'),
        ('RECEIVED', 'Delivery Received'),
        ('TRANSPORTING', 'Transporting'),
        ('DELIVERED', 'Delivered'),
        )

    CONDITION = (
         ('HEAT INTOLERANT', 'Heat intolerant'),
        ('WATER/MOIST INTOLERANT', 'Water/Moist intolerant'),
        ('PERISHABLE', 'Perishable'),
        ('FRAGILE', 'Fragile'),
    )

    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=20, null=True)
    condition = models.CharField(choices=CONDITION, max_length=30, null=True)
    driver = models.ForeignKey(to=Driver, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{str(self.owner.email)}"


