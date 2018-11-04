from django.contrib import admin

from .models import IncomeCategory,Income,Settings,ExpenseCategory,Expense

admin.site.register(IncomeCategory)
admin.site.register(Income)
admin.site.register(Settings)
admin.site.register(ExpenseCategory)
admin.site.register(Expense)