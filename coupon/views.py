from coupon.models import Coupon, Games
from django.views import generic
from coupon.forms import CouponForm
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.http import HttpResponse
from coupon.models import Winners

class CouponCreate(generic.CreateView):
    form_class = CouponForm
    template_name = 'coupon/coupon_form.html'

    def get_context_data(self, **kwargs):
        context = super(CouponCreate, self).get_context_data(**kwargs)
        #set some more context below.
        latest_game = Games.objects.latest('pk')
        context['latest_game'] = latest_game
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super(CouponCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('coupon_submitted', args=(self.object.pk,))


class CouponSubmitted(generic.DetailView):
    template_name = 'coupon/coupon_submitted.html'
    model = Coupon

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(CouponSubmitted, self).get(request, *args, **kwargs)

    def get_coupon_id(self, request, *args, **kwargs):
        self.object = self.get_object()
        return self.object.pk
    
    def get_context_data(self, **kwargs):
        context = super(CouponSubmitted, self).get_context_data(**kwargs)
        self.object = self.get_object()
        qs = Coupon.objects.get(pk=self.object.pk)
        context = {
            'coupon': qs,
            'object': self.object,
        }
        return context

class WinnersList(generic.ListView):

    def get(self, request, *args, **kwargs):        
        return super(WinnersList, self).get(request, *args, **kwargs)
    
    def get_queryset(self):
        return Winners.objects.all()