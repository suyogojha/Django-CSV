from django.db import models



class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name
    