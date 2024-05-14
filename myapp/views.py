from django.http import JsonResponse
from .models import MyModel
from .models import User
import json




def my_view(request):
    data = list(MyModel.objects.all().values())
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


def login_view(request):
    if request.method == 'POST':
        # 从 POST 请求中获取用户名和密码
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 检查用户名和密码是否为 admin 和 111111
        print('username',username)
        print('password',password)
        if username == 'admin' and password == '111111':
            # 登录成功
            return JsonResponse({'message': 'Login successful'}, status=200)
        else:
            # 登录失败，用户名或密码错误
            return JsonResponse({'error': 'Invalid username or password'}, status=400)
    else:
        # 不支持除 POST 以外的其他请求方法
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)



def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        if username and password and email:
            user = User.objects.create(username=username, password=password, email=email)
            return JsonResponse({'message': 'User created successfully', 'id': user.id}, status=201)
        else:
            return JsonResponse({'error': 'Missing username, password, or email'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


def home(request):
    return JsonResponse({"message": "Welcome to the API!"})
