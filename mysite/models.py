from django.db import models

class MyAccount(models.Model):
    moneyIn = models.IntegerField()
    moneyOut = models.IntegerField()

