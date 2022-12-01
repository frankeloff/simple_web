from django.shortcuts import render
from .models import Price, Car, Firm, Rate
from django.views.generic import ListView, DetailView
# Create your views here.

# class PriceView(ListView):
#     model = Price
#     template_name: str = "app/home.html"
#     context_object_name = 'price'
#     allow_empty: bool = True

    # def get_context_data(self, **kwargs):
    #     context = super(PriceView, self).get_context_data(**kwargs)
    #     context['car'] = Car.objects.all()
    #     context['firm'] = Firm.objects.all()
    #     context['rate'] = Rate.objects.all()
    #     # And so on for more models
    #     return context

class CarView(ListView):
    model = Car
    template_name: str = "app/home.html"
    context_object_name = 'car'
    allow_empty: bool = True

class ViewCar(DetailView):
    model = Car
    template_name: str = "app/views_car.html"
    context_object_name = 'car_item'
