from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter

from .serializers import(
    CategorySerializer,
    CustomerSerializer
)
from ..models import Category, Customer


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CustomerListAPIView(ListAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
