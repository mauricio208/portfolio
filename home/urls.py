from django.conf.urls import url
from home.views import *

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'paypalHowMuch', PaypalHowmuchView.as_view(), name='paypal_howmuch'),
]
