from django.db import models
from . import goods
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
register_user = get_user_model()


class Genre(models.Model):
    genre = models.CharField(max_length=30, primary_key=True)


class Technique(models.Model):
    technique = models.CharField(max_length=30, primary_key=True)


class Goods(models.Model):
    author = models.CharField(max_length=30)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    technique = models.ForeignKey(Technique, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    price = models.IntegerField()
    date = models.DateField()
    address = models.CharField(max_length=100)
    info = models.TextField()

    def dict_transform(self):
        goods_dict = {
            'author': self.author,
            'genre': self.genre.genre,
            'technique': self.technique.technique,
            'price': str(self.price - 0.01),
            'info': self.info,
            'title': self.title,
            'date': self.date,
            'id': str(self.id),
            'extra_id': 'modal-x-'+str(self.id),#<-
            'address': self.address
        }
        return goods_dict

    class Meta:
        verbose_name_plural = "Goods"

    def __str__(self):
        return self.title

