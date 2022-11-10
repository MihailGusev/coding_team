from typing import OrderedDict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import FoodSerializer, FoodListSerializer
from core.models import Food, FoodCategory


@api_view(['GET'])
def get_foods(request):
    # setup()
    foods = Food.objects.filter(is_publish=True).select_related()
    category_to_foods = dict()
    for f in foods:
        if f.category not in category_to_foods:
            category_to_foods[f.category] = []
        category_to_foods[f.category].append(f)

    data = []
    for c in category_to_foods:
        c_data = FoodListSerializer(c).data
        c_data['foods'] = FoodSerializer(category_to_foods[c], many=True).data
        data.append(c_data)
    

    return Response(data)


def setup():
    # return
    Food.objects.all().delete()
    FoodCategory.objects.all().delete()

    beverages = FoodCategory.objects.create(name_ru='Напитки', order_id=10)
    cola = Food.objects.create(category=beverages, internal_code=100, code=1, name_ru='Чай', description_ru='Чай 100гр', cost=123)
    tea = Food.objects.create(category=beverages, internal_code=200, code=2, name_ru='Кола', description_ru='Кола', cost=123)
    cola.additional.set([tea])
    Food.objects.create(category=beverages, internal_code=300, code=3, name_ru='Спрайт', description_ru='Спрайт', cost=123)
    Food.objects.create(category=beverages, internal_code=400, code=4, name_ru='Байкал', description_ru='Байкал', cost=123, is_publish=False)

    bakery = FoodCategory.objects.create(name_ru='Выпечка', order_id=20)
    Food.objects.create(category=bakery, internal_code=500, code=5, name_ru='Багет', description_ru='Багет', cost=456, is_publish=False)
    Food.objects.create(category=bakery, internal_code=600, code=6, name_ru='Пончик', description_ru='Пончик', cost=456, is_publish=False)
