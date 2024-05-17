# from myapp.models import User  # 导入你的用户模型
from myapp.models import User
# 查询数据库中是否存在指定的用户名和密码
user_exists = User.objects.filter(username='admin', password='asdzxc123').exists()

# 打印结果
print(user_exists)
