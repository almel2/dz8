from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField()

    def __str__(self):
        return f'ИМЯ: {self.first_name} ФАМИЛИЯ: {self.last_name} ' \
               f'ПОЧТА: {self.email}'
