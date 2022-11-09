from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import FoodSerializer, FoodListSerializer
from core.models import Food, FoodCategory

@api_view(['GET'])
def get_foods(request):
    return Response()
