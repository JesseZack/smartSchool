from django.db import models

from users.models import Student, Staff


class Discount(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    amount_or_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    discount_type = models.IntegerField(choices=(
        (1, 'Amount'),
        (2, 'Percentage')
    ))
    applicable_start_date = models.DateField()
    applicable_end_date = models.DateField()

    def __str__(self):
        return self.name


class FeeStructure(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    frequency = models.IntegerField(choices=(
        (1, 'Daily'),
        (2, 'Weekly'),
        (3, 'Monthly'),
        (4, 'Quarterly'),
        (5, 'Annually')
    ))
    discount = models.ForeignKey(Discount, on_delete=models.DO_NOTHING, null=True, blank=True)

    def amount_due(self):
        amount = float(self.amount) * float(self.discount.amount_or_percentage)
        return amount

    def __str__(self):
        return f'{self.name}'


class Invoice(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    invoice_date = models.DateField()
    due_date = models.DateField()
    status = models.IntegerField(choices=(
        (1, 'Unpaid'),
        (2, 'Partially Paid'),
        (3, 'Fully Paid')
    ))
    fees = models.ManyToManyField(FeeStructure)

    def total_amount(self):
        total = sum(fee.amount for fee in self.fees.all())
        return total

    def __str__(self):
        return f"Invoice for {self.student} - {self.invoice_date}"


class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    payment_date = models.DateField()
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20)
    transaction_reference = models.CharField(max_length=100)

    def __str__(self):
        return f"Payment for {self.invoice} - {self.payment_date}"


class LateFee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    late_fee_amount = models.DecimalField(max_digits=10, decimal_places=2)
    effective_start_date = models.DateField()
    effective_end_date = models.DateField()

    def __str__(self):
        return f"Late Fee for {self.student} - {self.invoice}"


class Receipt(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    payment_date = models.DateField()
    amount_received = models.DecimalField(max_digits=10, decimal_places=2)
    received_by = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Receipt for {self.student} - {self.invoice}"


class Refund(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    refund_date = models.DateField()
    amount_refunded = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.TextField()

    def __str__(self):
        return f"Refund for {self.student} - {self.invoice}"


class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class TransactionLog(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    action = models.PositiveIntegerField(choices=(
        (1, 'Invoice Created'),
        (2, 'Payment Received'),
        (3, 'Refund Issued')
    ))
    details = models.TextField()

    def __str__(self):
        return f"{self.date_time} - {self.user}: {self.action}"


class BankAccount(models.Model):
    account_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    swift_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.account_name} - {self.bank_name}"


class Expense(models.Model):
    expense_date = models.DateField()
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.expense_date} - {self.category}: {self.description}"


class Balance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def increase_balance(self, credit):
        self.amount += float(credit)

    def decrease_balance(self, debit):
        self.amount -= float(debit)

    def __str__(self):
        return f'{self.student.first_name}'
