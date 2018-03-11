from django.db import models
from games.models import Games

class Coupon(models.Model):
    coupon_tour = models.ForeignKey(Games, on_delete=models.CASCADE)
    coupon_id = models.CharField("Coupon id", primary_key=True, max_length=30)
    firstname = models.CharField("First Name", max_length=30)
    lastname = models.CharField("Surname", max_length=30)
    phone_number = models.CharField("Phone number", max_length=20)
    match1 = models.ForeignKey(Games, to_field='games_match1', related_name='match1', on_delete=models.CASCADE)
    match2 = models.ForeignKey(Games, to_field='games_match2', related_name='match2', on_delete=models.CASCADE)
    match3 = models.ForeignKey(Games, to_field='games_match3', related_name='match3', on_delete=models.CASCADE)
    bet1 = models.CharField("Bet 1", max_length=3)
    bet2 = models.CharField("Bet 2", max_length=3)
    bet3 = models.CharField("Bet 3", max_length=3)



    def __str__(self):
        return "Coupon {}".format(self.coupon_id)
