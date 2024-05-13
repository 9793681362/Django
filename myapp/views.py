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

def home(request):
    return JsonResponse({"message": "Welcome to the API!"})
