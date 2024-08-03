from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=50,verbose_name="Название таска")
    points = models.IntegerField(default=0,verbose_name="Баллы")

    def __str__(self):
        return self.name

class Basket(models.Model):
    task = models.ForeignKey(Task, models.SET_NULL)
    quantity = models.IntegerField(verbose_name="Количество тасков")
    point_of_received = models.IntegerField(verbose_name="Полученный балл")

class CompletedTask(models.Model):
    student = models.ForeignKey(User, models.SET_NULL)
    dateOfDeparture = models.DateField(verbose_name="Дата сдачи")
    basket = models.ForeignKey(Basket, models.SET_NULL)
    sum_of_points = models.ForeignKey(Basket, models.SET_NULL, verbose_name='Общий балл')





