from django.shortcuts import render
from django.views.generic.list import ListView
from toreports.models import Pacient

class PacientListView(ListView):
    model = Pacient
    template_name='home.html'
    def get_context_data(self, **kwargs):
        context = super(PacientListView, self).get_context_data(**kwargs)
        return context

    def post(self,request,*args, **kwargs):
        pass
