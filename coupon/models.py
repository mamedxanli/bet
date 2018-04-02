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