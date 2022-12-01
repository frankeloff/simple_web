from django.urls import path
from .views import CarView, ViewCar

urlpatterns = [
    # path('', PriceView.as_view(), name='home'),
    path('', CarView.as_view(), name='home'),
    path('car/<int:pk>/', ViewCar.as_view(), name='views_car'),
]