from django.db import models

# Create your models here.
class Profile(models.Model):
    MAX_FIRST_NAME_LENGTH = 15
    MAX_LAST_NAME_LENGTH = 15

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH
    )
    last_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH
    )

    budget = models.PositiveIntegerField(
        default=0
    )

    def remaining_budget(self):
        total_expenses = self.expense_set.aggregate(total=models.Sum('price'))['total'] or 0
        return self.budget - total_expenses