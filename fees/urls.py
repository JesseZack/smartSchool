from django.urls import path

from core_api.views.fee_views import ExpenseCategoryListCreateView, ExpenseListCreateView

app_name = 'fees'

urlpatterns = [
    path('expense_category/', ExpenseCategoryListCreateView.as_view(), name='expense-category'),
    path('expenses/', ExpenseListCreateView.as_view(), name='expense-list'),
]
