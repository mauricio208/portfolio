from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.template.loader import render_to_string
from toreports.models import *
import datetime as dt

class PacientListView(ListView):
    model = Pacient
    template_name='home_toreports.html'
    def get_context_data(self, **kwargs):
        context = super(PacientListView, self).get_context_data(**kwargs)
        return context

    def ajax_save_pacient(request):
        name=request.POST.get('name')
        if name:
            p=Pacient(name=name,first_meet_on=dt.datetime.now())
            p.save()
            pacient_template=render_to_string('pacient.htm',{'pacient':p})
            return HttpResponse(pacient_template)

    def ajax_save_report(request):
        data=request.POST 
        date=data.get('date')
        text=data.get('report')
        pacient_id=data.get('pacient_id')
        if not pacient_id:
            HttpResponse("Wrong id")
        if pacient_id and date:
            r=Report(date=date,text=text)
            r.save()
            pacient=Pacient.objects.get(id=pacient_id)
            pacient.reports.add(r)
            pacient.save()
            report_template=render_to_string('report.htm',{'report':r})
            return HttpResponse(report_template)

    def ajax_edit_report(request):
        data=request.POST 
        date=data.get('date')
        text=data.get('report')
        report_id=data.get('pacient_id')
        if not report_id:
            HttpResponse("Wrong id")
        report=Report.objects.get(id=report_id)
        if date:
            report.date=date
        if text:
            report.text=text
        report.save()
        report_template=render_to_string('report.htm',{'report':report})
        return HttpResponse(report_template)

    def ajax_load_reports(request):
        pacient_id=request.GET.get('pacient_id')
        if not pacient_id:
            HttpResponse("Wrong id")
        if pacient_id:
            pacient=Pacient.objects.get(id=pacient_id)
            reports_list_template=render_to_string('reports_list.htm',{'pacient':pacient})
            return HttpResponse(reports_list_template)
