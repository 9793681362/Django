from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password

from .models import OpenT
from .models import User
import json




def my_view(request):
    data = list(OpenT.objects.all().values())
    return JsonResponse(data, safe=False)


def test_data_api(request):
    data = [
        {'id': 1, 'name': 'Item 1', 'description': 'Description for Item 1'},
        {'id': 2, 'name': 'Item 2', 'description': 'Description for Item 2'},
        {'id': 3, 'name': 'Item 3', 'description': 'Description for Item 3'},
        # 可以添加更多的测试数据
    ]
    return JsonResponse(data, safe=False)

def get_nav_value(request):
    nav_value = [
        {'id': 0, 'nav': 'Home', 'content': '\uF425', 'route': '/home'},
        {'id': 1, 'nav': 'English', 'content': '\uF658', 'route': '/english'},
        {'id': 2, 'nav': 'Master', 'content': '\uF7CD', 'route': '/master'},
        {'id': 3, 'nav': 'Javascript', 'content': '\uF74C', 'route': '/javascript'},
        {'id': 4, 'nav': 'Vue', 'content': '\uF8C4', 'route': '/vue'},
        {'id': 5, 'nav': 'Python', 'content': '\uF75C', 'route': '/python'},
        {'id': 6, 'nav': 'Django', 'content': '\uF7CE', 'route': '/django'},
        {'id': 7, 'nav': '', 'content': ''},
        {'id': 8, 'nav': 'GitHub', 'content': '\uF3ED', 'route': '/github'},
        {'id': 10, 'nav': 'Plane', 'content': '\uF1A2', 'route': 'plane'},
        {'id': 11, 'nav': '', 'content': ''}
    ]
    return JsonResponse(nav_value, safe=False)


from django.contrib.auth import authenticate
from django.http import JsonResponse
import json


from django.contrib.auth import authenticate
from django.http import JsonResponse

from myapp.models import User  # 导入自定义的用户模型


from django.contrib.auth.hashers import check_password

def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print("请求体内容：", data)
        username = data.get('username')
        password = data.get('password')
        print("我输入的账号密码",username,password)

        # 查询自定义用户模型
        users = User.objects.filter(username=username)
        print("查询结果：", users)

        if users.exists():
            user = users.first()
            print("我输入的密码:",type(password),password)
            print("数据库中存储的密码：", type(user.password),user.password)

            if (password == user.password):
            # if check_password(password, user.password):
                # 密码匹配，认证成功
                return JsonResponse({'message': 'Login successful'}, status=200)
            else:
                # 密码不匹配，认证失败
                return JsonResponse({'error': 'Invalid username or password'}, status=400)
        else:
            # 用户不存在
            return JsonResponse({'error': 'Invalid username or password'}, status=400)
    else:
        # 不支持除POST以外的其他请求方法
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        phone_number = data.get('phone_number')
        print('username',username)
        print('password',password)
        print('email',email)
        print('phone_number',phone_number)


        if username and password and email:
            user = User.objects.create(username=username, password=password, email=email,phone_number=phone_number)
            return JsonResponse({'message': 'User created successfully', 'id': user.id}, status=200)
        else:
            return JsonResponse({'error': 'Missing username, password, or email'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


def home(request):
    return JsonResponse({"message": "Welcome to the API!"})
