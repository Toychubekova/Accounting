from django.db import models
from user import utils

class Headman(models.Model):
    name = models.CharField(max_length=100, verbose_name="ФИО")
    phone = models.CharField("Номер телефона", max_length=200, null=True, blank=True)
    dateOfBirth = models.DateField(verbose_name="День рождение", null=True, blank=True)
    PIN = models.IntegerField()
    user_type = models.CharField("Тип пользователя", max_length=50, choices=utils.USER_TYPE)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="ФИО")
    addressOfStudy = models.CharField(max_length=50, verbose_name="Адрес учебы",null=True, blank=True)
    dateOfBirth = models.DateField(verbose_name='День рождение', null=True, blank=True)
    user_type = models.CharField("Тип пользователя", max_length=50, choices=utils.USER_TYPE)

    def __str__(self):
        return self.name

class Team (models.Model):
    headman = models.ForeignKey(Headman, models.SET_NULL)
    student = models.ForeignKey(Student, models.SET_NULL)
    name = models.CharField(max_length=50, verbose_name="Название команды")
    addressOfJob = models.CharField(max_length=50, verbose_name='Адрес работы', null=True, blank=True)
    amount = models.IntegerField(verbose_name='Количество участников', null=True, blank=True)
    dateOfPayment = models.DateField(verbose_name='Дата оплаты за аренду офиса', null=True, blank=True)
    summRent = models.IntegerField(verbose_name='Сумма аренды', null=True, blank=True)

    def __str__(self):
        return self.name

