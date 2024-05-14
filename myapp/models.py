from django.db import models


class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'login'