from django.conf.urls import url
from home.views import *
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'paypalHowMuch$', PaypalHowmuchView.as_view(), name='paypal_howmuch'),
    url(r'paypal.*$',RedirectView.as_view(url='paypalHowMuch', permanent=False), name='to_paypal'),
    url(r'calc.*$',RedirectView.as_view(url='paypalHowMuch', permanent=False), name='to_paypal_calc'),
]
