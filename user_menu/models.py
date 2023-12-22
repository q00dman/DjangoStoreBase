from django.db import models
from apps.models import Goods, register_user


class Comment(models.Model):
    good = models.ForeignKey(Goods,  on_delete=models.CASCADE)
    date = models.DateField()
    user_name = models.ForeignKey(register_user,  on_delete=models.CASCADE)
    comment = models.TextField()


class Order(models.Model):
    good = models.ForeignKey(Goods,  on_delete=models.CASCADE)
    buyer = models.ForeignKey(register_user,  on_delete=models.CASCADE)
    address = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=13)

