from django.db import models


class Computer(models.Model):
    name = models.CharField(max_length=255)


class Disk(models.Model):
    name = models.CharField(max_length=255)
    cost = models.CharField(max_length=255)
    computer_id = models.ForeignKey(Computer, on_delete=models.CASCADE, null=True)
