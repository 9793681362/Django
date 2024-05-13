from django.http import JsonResponse
from .models import MyModel

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

def home(request):
    return JsonResponse({"message": "Welcome to the API!"})
