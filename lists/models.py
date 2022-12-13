from django.db import models


class List(models.Model):
    ...


class Item(models.Model):
    text = models.TextField(default="")
    list = models.ForeignKey(to=List, on_delete=models.CASCADE, default=None)
