from django.db.models import (
    Model,
    IntegerField,
    CharField,
)
from django.core.validators import MaxValueValidator, MinValueValidator

class Thing(Model):
    name = CharField(unique=True, blank=False, max_length=30)
    description = CharField(unique=False, blank=True, max_length=120)
    quantity = IntegerField(unique=False, validators=[MaxValueValidator(100), MinValueValidator(0)])