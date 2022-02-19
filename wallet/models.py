from django.db import models
class Wallet(models.Model):
    raddress = models.CharField(max_length=60)
    def __str__(self):
        return self.name
