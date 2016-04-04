from django.shortcuts import render_to_response
from django.views.generic.base import View,TemplateView

class HomeView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context


class PaypalHowmuchView(View):
	def how_much_send_for(self,total_a_enviar, tasa_pais, tasa_fija) :
		# import pudb; pudb.set_trace()
		tasa_pais=tasa_pais/100
		i = total_a_enviar/(1-tasa_pais)
		error= lambda i: (i-(i*tasa_pais+tasa_fija))-total_a_enviar
		valor_iteracion= lambda x :x-x*(tasa_pais+(tasa_fija/x))
		while valor_iteracion(i)<total_a_enviar:
			i+=0.01
		return i

	def get (self,request):
		# import pudb; pudb.set_trace()
		total=request.GET.get('total_a_enviar',None)
		tp=request.GET.get('tasa_pais',None)
		tf=request.GET.get('tasa_fija',None)

		context={'total':None,'error':None}
		if tp and total and tf:
			context['total']=float('%.2f' %self.how_much_send_for(float(total),float(tp), float(tf)))+0.01
		else:
			context['error']='You must submit all required data'

		context['total_a_enviar']=total
		context['tasa_pais']=tp
		context['tasa_fija']=tf
		return render_to_response(template_name='paypal_t.html',context=context)


