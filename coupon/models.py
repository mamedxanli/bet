from django.db import models

class Coupon(models.Model):
    coupon_id = models.CharField("Coupon id", max_length=30)
    firstname = models.CharField("First Name", max_length=30, help_text=
        "First Name")
    lastname = models.CharField("Surname", max_length=30, help_text=
        "Surname")
    phone_number = models.CharField("Phone number", max_length=20, help_text=
        "Phone number")
    match1 = models.CharField("Match 1", max_length=50,help_text=
        "First match")
    match2 = models.CharField("Match 2", max_length=50,help_text=
        "Second match")
    match3 = models.CharField("Match 3", max_length=50,help_text=
        "Third match")
    match4 = models.CharField("Match 4", max_length=50,help_text=
        "Fourth match")
    match5 = models.CharField("Match 5", max_length=50)
    match6 = models.CharField("Match 6", max_length=50,help_text=
        "Sixth match")
    match7 = models.CharField("Match 7", max_length=50,help_text=
        "Seventh match")
    match8 = models.CharField("Match 8", max_length=50,help_text=
        "Eighth match")
    match9 = models.CharField("Match 9", max_length=50,help_text=
        "Ninth match")
    match10 = models.CharField("Match 10", max_length=50,help_text=
        "Tenth match")
    match11 = models.CharField("Match 11", max_length=50,help_text=
        "Eleventh match")
    match12 = models.CharField("Match 12", max_length=50,help_text=
        "Twelfth match")
    bet1 = models.CharField("Bet 1", max_length=3,help_text=
        "First bet")
    bet2 = models.CharField("Bet 2", max_length=3,help_text=
        "Second bet")
    bet3 = models.CharField("Bet 3", max_length=3,help_text=
        "Third bet")
    bet4 = models.CharField("Bet 4", max_length=3,help_text=
        "Fourth bet")
    bet5 = models.CharField("Bet 5", max_length=3,help_text=
        "Fifth bet")
    bet6 = models.CharField("Bet 6", max_length=3,help_text=
        "Sixth bet")
    bet7 = models.CharField("Bet 7", max_length=3,help_text=
        "Seventh bet")
    bet8 = models.CharField("Bet 8", max_length=3,help_text=
        "Eighth bet")
    bet9 = models.CharField("Bet 9", max_length=3,help_text=
        "Ninth bet")
    bet10 = models.CharField("Bet 10", max_length=3,help_text=
        "Tenth bet")
    bet11 = models.CharField("Bet 11", max_length=3,help_text=
        "Eleventh bet")
    bet12 = models.CharField("Bet 12", max_length=3,help_text=
        "Twelfth bet")


    def __str__(self):
        return "Coupon {}".format(self.coupon_id)
