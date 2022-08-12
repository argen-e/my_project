from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name}  {self.surname}"