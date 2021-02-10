from django.urls import path

from .api_views import(
    CategoryListAPIView,
    NotebookListAPIView,
    SmartphoneListAPIView,
    SmartphoneDetailAPIView,
    CustomerListAPIView
)


urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='categories'),
    path('notebooks/', NotebookListAPIView.as_view(), name='notebooks'),
    path('smartphones/', SmartphoneListAPIView.as_view(), name='smartphones_list'),
    path('smartphones/<str:id>', SmartphoneDetailAPIView.as_view(), name='smartphone_detail'),
    path('customers/', CustomerListAPIView.as_view(), name='customers_list'),
]
