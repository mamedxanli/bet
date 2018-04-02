from django.db import models
from games.models import Games
from django.urls import reverse

class Coupon(models.Model):
    #This field can be made non-editable by adding editable=False to the FK arguments. 
    #In this case we made it through forms so no need for that.
    coupon_tour = models.ForeignKey(Games, on_delete=models.CASCADE)
    firstname = models.CharField("First Name", max_length=30)
    lastname = models.CharField("Surname", max_length=30)
    phone_number = models.CharField("Phone number", max_length=20)
    bet1 = models.CharField("Bet 1", max_length=3)
    bet2 = models.CharField("Bet 2", max_length=3)
    bet3 = models.CharField("Bet 3", max_length=3)
    coupon_amount = models.IntegerField("Amount", default=0, editable=False)


    def __str__(self):
        return "Coupon {}".format(self.pk)

    def get_absolute_url(self):
        """
        Handy way of getting the url of the object to its detail view page
        """
        return reverse('coupon')
    
    @property
    def _get_coupon_amount(self):
        amount = len(self.bet1) * len(self.bet2) *len(self.bet3)
        return amount 

    def save(self, *args, **kwargs):
        self.coupon_amount = self._get_coupon_amount
        super(Coupon, self).save(*args, **kwargs)


class WinnerCoupon(models.Model):
    tour = models.IntegerField("Tour", primary_key=True, default=0)
    result1 = models.IntegerField("Game 1", default=3)
    result2 = models.IntegerField("Game 2", default=3)
    result3 = models.IntegerField("Game 3", default=3)

    def __str__(self):
        return "Results for tour {}".format(self.tour)

    winners = ''
    

    def find_winner(self):
        self.object = self.get_object()
        all_coupons = Coupon.objects.filter(coupon_tour=self.objects.tour)
        for coupon in all_coupons:
            if self.result1 in coupon.bet1:
                pass
            elif self.result2 in coupon.bet2:
                pass
            elif self.result3 in coupon.bet3:
                winners += coupon.pk
                return winners
            else:
                continue
