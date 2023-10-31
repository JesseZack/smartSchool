from rest_framework.generics import ListCreateAPIView

from core_api.serializers.fees_serializer import ExpenseCategorySerializer, ExpenseSerializer
from fees.models import ExpenseCategory, Expense


class ExpenseCategoryListCreateView(ListCreateAPIView):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer


class ExpenseListCreateView(ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
