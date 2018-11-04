from django.db import models

from .model_functions import *

class Settings(models.Model):
	name = models.CharField(max_length=250)
	value = models.CharField(max_length=1000)

	def __str__(self):
		return self.name+' : '+self.value

class Menu(models.Model):

	name = models.CharField(max_length=250)
	url = models.CharField(max_length=1000)

class IncomeCategory(models.Model):
	name = models.CharField(max_length=200)
	icon = models.CharField(max_length=250,choices=get_fontawesome_list())
	color = models.CharField(max_length=20)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Income Category'
		verbose_name_plural = 'Income Categories'

class Income(models.Model):
	amount = models.DecimalField(max_digits=12,decimal_places=2)
	date = models.DateTimeField()
	cat = models.ForeignKey(IncomeCategory,on_delete=models.SET_NULL,null=True)

	def __str__(self):
		
		output = str(self.amount)

		if self.cat is not None:
			output += ' '+self.cat.name

		return output

class ExpenseCategory(models.Model):
	name = models.CharField(max_length=200)
	icon = models.CharField(max_length=250,choices=get_fontawesome_list())
	color = models.CharField(max_length=20)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Expense Category'
		verbose_name_plural = 'Expense Categories'

class Expense(models.Model):
	amount = models.DecimalField(max_digits=12,decimal_places=2)
	date = models.DateTimeField()
	cat = models.ForeignKey(ExpenseCategory,on_delete=models.SET_NULL,null=True)

	def __str__(self):
		cat = ExpenseCategory.objects.get(pk=self.cat.id)
		return str(self.amount)+' '+cat.name




