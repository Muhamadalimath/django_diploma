from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apiapp.views import BasketModelView, BannerModelView, Categories, ProductsModelView, OrdersModelView
from .views import LoginView, logout, LimitedProductsView, PopularProductsView, PaymentAPIView

from apiapp.views import TagModelView

router = DefaultRouter()
router.register('basket', BasketModelView)
router.register('banners', BannerModelView)
router.register('tags', TagModelView)
router.register('catalog', ProductsModelView)
router.register('orders', OrdersModelView)
urlpatterns = [
    path('', include(router.urls)),
    path('sign-in', LoginView.as_view()),
    path('sign-out', logout),
    path('categories', Categories.as_view()),
    path('products/popular', PopularProductsView.as_view()),
    path('products/limited', LimitedProductsView.as_view()),
    path('payment', PaymentAPIView.as_view()),
]
