from rest_framework import serializers

from fees.models import Discount, FeeStructure, Invoice, Payment, LateFee, Receipt, Refund, ExpenseCategory, TransactionLog, \
    BankAccount, Expense, Balance


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = (
            'name',
            'description',
            'amount_or_percentage',
            'discount_type',
            'applicable_start_date',
            'applicable_end_date',
        )


class FeeStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeStructure
        fields = (
            'name',
            'description',
            'amount',
            'frequency',
            'discount'
        )


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = (
            'students',
            'invoice_date',
            'due_date',
            'status',
            'fees'
        )


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'invoice',
            'payment_date',
            'amount_paid',
            'payment_method',
            'transaction_reference'
        )


class LateFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LateFee
        fields = (
            'student',
            'invoice',
            'late_fee_amount',
            'effective_start_date',
            'effective_end_date'
        )


class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = (
            'student',
            'invoice',
            'payment_date',
            'amount_received',
            'received_by'
        )


class RefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refund
        fields = (
            'student',
            'invoice',
            'refund_date',
            'amount_refunded',
            'reason'
        )


class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = (
            'name',
            'description'
        )


class TransactionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionLog
        fields = (
            'date_time',
            'user',
            'action',
            'details'
        )


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = (
            'account_name',
            'account_number',
            'bank_name',
            'branch',
            'swift_code'
        )


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = (
            'expense_date',
            'description',
            'amount',
            'category'
        )


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = (
            'student',
            'amount'
        )