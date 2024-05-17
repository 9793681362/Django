from django.db import models

class OpenT(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.TextField()

    def __str__(self):
        return self.field1


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField(null=True, blank=True)  # 新添加的age字段
    phone_number = models.CharField(max_length=20, null=True, blank=True)  # 添加电话号码字段

    REQUIRED_FIELDS = ['username', 'password']  # 定义必需的字段

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'admin_user'