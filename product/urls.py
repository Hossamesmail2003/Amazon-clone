from django.urls import path
from .views import ProductList , ProductDetail ,BrandList,BrandDetail,queryset_debug
from .api import  ProductListPI, ProductDetailAPI , BrandDetailAPI , BrandListAPI
urlpatterns = [
    path('', ProductList.as_view()),
    path('debug', queryset_debug),
    path('<slug:slug>', ProductDetail.as_view()),
    path('brands/', BrandList.as_view()),
    path('brands/<slug:slug>',BrandDetail.as_view()),


    #api
    path('api/list', ProductListPI.as_view()),
    path('api/list/<int:pk>', ProductDetailAPI.as_view()),



    path('brands/api/list', BrandListAPI.as_view()),
    path('brands/api/list/<int:pk>', BrandDetailAPI.as_view()),
]
