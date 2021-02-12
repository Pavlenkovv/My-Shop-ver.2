from django.urls import path

from .api_views import(
    CategoryListAPIView,
    CustomerListAPIView
)


urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='categories'),
    path('customers/', CustomerListAPIView.as_view(), name='customers_list'),
]
