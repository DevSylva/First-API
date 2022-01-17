from django.db import models
from authentication.models import User
from driver.models import Driver

# Create your models here.
class Orders(models.Model):

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

    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE
    )
    status = models.CharField(
        choices=STATUS, max_length=20, default=STATUS[0]
    )
    condition = models.CharField(
        choices=CONDITION, max_length=30, null=True
    )
    driver = models.ForeignKey(
        to=Driver, on_delete=models.CASCADE, null=True)
    address = models.CharField(
        max_length=50
    )
    price = models.DecimalField(
        max_digits=7, decimal_places=2
    )
    receiver = models.CharField(
        max_length=50, verbose_name="receiver's name"
    )
    date_created = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return f"{str(self.user.email)}"


    class Meta:
        verbose_name="Orders Made"
        verbose_name_plural="Orders Made"


