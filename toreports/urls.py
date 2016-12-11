"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from toreports.views import PacientListView

urlpatterns = [
    url(r'^$', PacientListView.as_view(), name='pacientlist'),
    url(r'^ajax_save_pacient$', PacientListView.ajax_save_pacient, name='ajax_save_pacient'),
    url(r'^ajax_save_report$', PacientListView.ajax_save_report, name='ajax_save_report'),
    url(r'^ajax_load_reports$', PacientListView.ajax_load_reports, name='ajax_load_reports'),

]
