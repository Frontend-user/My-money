from django import forms

class CategoryForm(forms.Form):
    text = forms.CharField(max_length=200)

class ExpenseForm(forms.Form):
    expense_text = forms.CharField(max_length=400)
    expense_number = forms.CharField(max_length=20)
