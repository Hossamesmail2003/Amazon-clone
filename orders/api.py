from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .serializers import CartSerializer,OrderDetailSerializer , OrderListSerializer, OrderProductsSerializer
from .models import Cart,CartDetail , Order , OrderDetail , Coupon
from product.models import Product
import datetime



class CartDetailCreatAPI(generics.GenericAPIView):
    serializer_class = CartSerializer

    def get(self,request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        cart,created = Cart.objects.get_or_create(user=user,status='InProgress')
        data = CartSerializer(cart).data
        return Response({'cart':data})



    def post(self,request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        product = Product.objects.get(id=request.data['product_id'])
        quantity = int(request.data['quantity'])
        cart = Cart.objects.get(user=user,status='InProgress')
        cart_detail,created = CartDetail.objects.get_or_create(cart=cart , product=product)
        cart_detail.quantity = quantity
        cart_detail.total =round(quantity * product.price, 2) 
        cart_detail.save()
        cart = Cart.objects.get(user=user,status='InProgress')
        data = CartSerializer(cart).data
        return Response({'message':'product added successfully', 'cart':data})



    def delete(self,request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        cart_detail = CartDetail.objects.get(id=request.data['cart_detail_id'])
        cart_detail.delete()
        cart = Cart.objects.get(user=user,status='InProgress')
        data = CartSerializer(cart).data
        return Response({'message':'product deleted successfully', 'cart':data})
    



class OrderListAPI(generics.ListAPIView):
    serializer_class = OrderListSerializer
    queryset = Order.objects.all()

    def list(self, request, *args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        queryset = self.get_queryset().filter(user=user)
        data = OrderListSerializer(queryset,many=True).data
        return Response(data)

    # def get_queryset(self):
    #     queryset = super(OrderListAPI,self).get_queryset()
    #     user = User.objects.get(username=self.kwargs['username'])
    #     queryset = queryset.filter(user=user)
    #     return queryset

class OrderDetailAPI(generics.RetrieveAPIView):
    serializer_class = OrderListSerializer
    queryset = Order.objects.all()



class CreateOrderAPI(generics.GenericAPIView):
    def get(self,request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        cart = Cart.objects.get(user=user,status='InProgress')
        cart_detail= CartDetail.objects.all().filter(cart=cart)
        #cart --> order
        new_order = Order.objects.create(
            user = user,
            coupon = cart.coupon,
            total_after_coupon = cart.total_after_coupon
        )



        #cart_detail --> order_detail --> loop
        for object in cart_detail:
            OrderDetail.objects.create(
                order = new_order,
                product = object.product,
                quantity = object.quantity,
                price = object.product.price,
                total = round(int(object.quantity)*object.product.price,2)

            )
        cart.status = 'Completed'
        cart.save()
        return Response({'message': 'Order created successfully'})



class ApplyCouponAPI(generics.GenericAPIView):
    def post(self,request,*args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        cart = Cart.objects.get(user=user,status='InProgress')
        coupon = get_object_or_404(Coupon,code=request.data['coupon_code'])

        if coupon and coupon.quantity > 0 :
            today_date = datetime.datetime.today().date()
            if today_date >= coupon.start_date and today_date <= coupon.end_date:
                coupon_value = cart.cart_total()* coupon.discount /100
                cart_total = cart.cart_total() - coupon_value
                coupon.quantity -=1
                coupon.save()
                cart.coupon = coupon
                cart.total_after_coupon = cart_total
                cart.save()
                cart = Cart.objects.get(user=user,status='InProgress')
                data = CartSerializer(cart).data
                return Response({'message':'coupon applied successfully','cart':data})
            else:
                Response({'message':'coupon date are not valid'})
        else:
            return Response({'message':'no coupon found'})


