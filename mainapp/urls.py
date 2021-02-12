from django.urls import path
from .views import(
    BaseView,
    ProductDetailView,
    CategoryDetailView,
    CartView,
    AddToCardView,
    DeleteFromCartView,
    ChangeQuantityView,
    CheckoutView,
    MakeOrderView,
    LoginView
)


urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('products/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<str:slug>/', AddToCardView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<str:slug>/', DeleteFromCartView.as_view(), name='delete_from_cart'),
    path('change-quantity/<str:slug>/', ChangeQuantityView.as_view(), name='change_quantity'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('make-order/', MakeOrderView.as_view(), name='make_order'),
    path('login/', LoginView.as_view(), name='login'),
]
