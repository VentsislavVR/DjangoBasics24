from django.core.exceptions import ValidationError
from django.db import models


def non_empty_spaces(value):
    if ' ' in value:
        raise ValidationError('Spaces are not allowed.')

class Department(models.Model):
    name = models.CharField(max_length=100)

# Create your models here.
class Employee(models.Model):
    MAX_FIRST_NAME_LENGTH = 35
    ROLES = (
        (1, 'Developer'),
        (2, 'Manager'),
        (3, 'HR'),
    )

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        blank=False,
        null=False,
        validators=(non_empty_spaces,),

    )
    last_name = models.CharField(
        max_length=35,
        blank=False,
        null=False,
    )
    role = models.IntegerField(
        choices=ROLES,
    )
    department = models.ForeignKey(
        Department,on_delete=models.DO_NOTHING,
        null=True,
    )
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
