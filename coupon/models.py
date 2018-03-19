from django.db import models
from games.models import Games

class Coupon(models.Model):
    coupon_tour = models.ForeignKey(Games, on_delete=models.CASCADE)
    firstname = models.CharField("First Name", max_length=30)
    lastname = models.CharField("Surname", max_length=30)
    phone_number = models.CharField("Phone number", max_length=20)
    bet1 = models.CharField("Bet 1", max_length=3)
    bet2 = models.CharField("Bet 2", max_length=3)
    bet3 = models.CharField("Bet 3", max_length=3)



    def __str__(self):
        return "Coupon {}".format(self.id)
