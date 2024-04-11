from django.contrib.auth import login, logout
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from catalog.models import Banner, Tag, Category, Product
from orders.models import Order
from . import serializers
from .filtersets import CatalogFilter
from .paginators import CustomPagination
from .serializers import BasketSerializer, BasketBaseSerializer, BannersSerializer, TagSerializer, CategorySerializer, \
    CatalogSerializer, OrderSerializer
from basket.models import Basket

class BasketModelView(viewsets.ModelViewSet):
    queryset = Basket.objects.all()

    def get_serializer_class(self):
        if self.action in ['create']:
            return BasketSerializer
        return BasketBaseSerializer


class BannerModelView(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannersSerializer


class TagModelView(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ProductsModelView(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = CatalogSerializer
    pagination_class = CustomPagination
    filterset_class = CatalogFilter


class OrdersModelView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        print(request.data)

        serializer = serializers.LoginSerializer(data=self.request.data,
                                                 context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)


class Logout(APIView):
    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class Categories(APIView):
    def get(self, request):
        categories = Category.objects.all()
        return Response(CategorySerializer(categories, many=True).data)
class PopularProductsView(APIView):
    def get(self, request):
        products = Product.objects.get(limited_edition=True)
        return Response(ProductSerializer(products, many=True).data)
class LimitedProductsView(APIView):
    def get(self, request):
        products = Product.objects.all()[:16:]
        return Response(ProductSerializer(products, many=True).data)


class PaymentAPIView(APIView):
    def post(self, request):
        payment_method = request.data.get('payment_method')

        if payment_method == 'card':
            card_number = request.data.get('card_number')

            if len(card_number) <= 8 and card_number.isdigit() and int(card_number) % 2 == 0:
                return Response({'message': 'Waiting for payment confirmation from the payment system'},
                                status=status.HTTP_200_OK)

        elif payment_method == 'random_account':
            random_account = request.data.get('random_account')

            if len(random_account) <= 8 and random_account.isdigit() and int(random_account) % 2 == 0:
                return Response({'message': 'Waiting for payment confirmation from the payment system'},
                                status=status.HTTP_200_OK)

        return Response({'message': 'Invalid payment details'}, status=status.HTTP_400_BAD_REQUEST)