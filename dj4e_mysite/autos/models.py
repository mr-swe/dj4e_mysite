from django.core.validators import MaxLengthValidator
from django.db import models


# Create your models here.

class Make(models.Model):
    name = models.CharField(
        max_length=200,
        help_text='Enter a Make',
        validators=[MaxLengthValidator(2, 'Enter at least two character')]
    )

    def __str__(self):
        return self.name


class Autos(models.Model):
    nickname = models.CharField(
        max_length=200,
        help_text='Enter Nickname',
        validators=[MaxLengthValidator(2, "Nickname must be greater than 1 character")]
    )
    mileage = models.PositiveIntegerField()
    comments = models.CharField(max_length=300)
    make = models.ForeignKey(Make, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nickname
