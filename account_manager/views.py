from django.shortcuts import render
from django.views.generic.base import TemplateView

from .models import Income,IncomeCategory,Settings
from .helper_functions import *

class IndexView(TemplateView):

	template_name = 'account_manager/index.html'
	
	def get_context_data(self,**kwargs):

		context = super().get_context_data(**kwargs)
		context['last_incomes'] = Income.objects.order_by('-date')[:10]
		context['currency'] = get_setting('currency','$')
		
		return context
	