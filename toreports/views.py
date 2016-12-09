from django.shortcuts import render
from django.views.generic.list import ListView
from toreports.models import *
import datetime as dt

class PacientListView(ListView):
    model = Pacient
    template_name='home_toreports.html'
    def get_context_data(self, **kwargs):
        context = super(PacientListView, self).get_context_data(**kwargs)
        return context

    def post(self,request,*args, **kwargs):
        name=request.POST.get('name')
        if name:
            p=Pacient(name=name,first_meet_on=dt.datetime.now())
            p.save()

        return render('home_toreports.html')
