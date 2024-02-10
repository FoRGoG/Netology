from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    #id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=25)
    # image = models.CharField(max_length=50)
    # release_date = models.CharField(max_length=50)
    # lte_exists = models.CharField(max_length=50)
    # slug = models.SlugField(max_length=50)
    # pass
