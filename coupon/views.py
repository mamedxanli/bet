from coupon.models import Coupon
from django.views import generic
from coupon.forms import CouponForm
from django.shortcuts import get_object_or_404, render

"""
def post_coupon(request):
    if request.method == "POST":
        form = CouponForm(request.POST)
        if form.is_valid():
            post_data = form.save(commit=True)
            post_data.timestamp = timezone.now()
            post_data.save()

    else:
        form = CouponForm()

    return render(request, "coupon_list.html", {'form': form})

"""


class CouponCreate(generic.CreateView):
    model = Coupon
    form_class = CouponForm
"""
    def show_coupon(self, request):
        coupon = get_object_or_404(Coupon)
        return render(request, 'coupon/coupon_list.html', {'coupon': coupon})
"""



"""
Example:
# myapp/views.py
from django.core.shortcuts import render, redirect
from django import forms
from django.utils import timezone

from .forms import MyModelForm


def add_model(request):

    if request.method == "POST":
        form = MyModelForm(request.POST)
        if form.is_valid():

            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('victory')
    else:
        form = MyModelForm()

    return render(request, "my_template.html", {'form': form})

"""

""""
Example of db query:
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


"""
