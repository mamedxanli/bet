from django.contrib import admin
from coupon.models import Coupon, Games, WinnerCoupon

"""
This code will add extra drop down button to admin/coupon

@admin.register(Games)
class FindWinner(admin.ModelAdmin):
    #On admin page of Coupon we can visualize properties using the following syntax:
    list_display = ['pk', 'coupon_tour', 'coupon_amount', 'firstname', 'lastname', 'phone_number']
    list_filter = ( 'publish', )
    search_fields = ('pk',)
    #prepopulated_fields = {'firstname': ('id',)}
    #raw_id_fields = ('coupon_tour',)
    date_hierarchy = 'publish'
    ordering = ['publish']
    actions = [find_winner]
"""
admin.register(Games)
admin.site.register(Coupon)
admin.site.register(WinnerCoupon)

