from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Product,ProductImages,Brand,Review
from django.db.models import Q,F,Value
from django.db.models.aggregates import Max,Min,Count,Avg,Sum



def queryset_debug(request):
    #data = Product.objects.select_related('brand').all()  # prefetch_related = many to many
    # filter
    #data = Product.objects.filter(price__gt= 100)  # greater than
    #data = Product.objects.filter(price__gte= 70)  # greater than or equal
    #data = Product.objects.filter(price__lte= 70)  # less than or equal
    #data = Product.objects.filter(price__range= (70,100) ) # range
    # navigate relation
    #data = Product.objects.filter(brand__name= 'apple') 
    # filter with text
    #data = Product.objects.filter(name__contains='Harris') 
    #data = Product.objects.filter(name__startswith='James') 
    #data = Product.objects.filter(name__endswith='Rodriguez') 
    #data = Product.objects.filter(tags__isnull= True) 
    #data = Review.objects.filter(created_at__year = 2024) 
    #data = Review.objects.filter(created_at__month = 9) 
    # filter 2 values
    #data = Product.objects.filter(price__gt= 80 , quantity__lt= 10) # and
    #data = Product.objects.filter(
    #    Q(price__gt= 80) |
    #    Q(quantity__lt= 10)

    #) # or
    #data = Product.objects.filter(
    #    Q(price__gt= 80) &
    #    ~Q(quantity__lt= 10) # not less than

    #) # and
    # field lookup
    #data = Product.objects.filter(price = F('quantity'))

    #data = Product.objects.all().order_by('name') # order ABC
    #data = Product.objects.all().order_by('-name') # order zyx
    #data = Product.objects.all().order_by('name').reverse() # order zyx
    #data = Product.objects.order_by('name','quantity')# order 
    #data = Product.objects.order_by('name','-quantity')# order 


    #data = Product.objects.earliest('name') # first 
    #data = Product.objects.latest('name') # last 

    # slice
    #data = Product.objects.all() [:10] # first 10 objects

    # select columns
    #data = Product.objects.values('name', 'price','brand__name')
    #data = Product.objects.values_list('name', 'price','brand__name')

    # remove duplicate
    #data = Product.objects.all().distinct()

    # only
    #data = Product.objects.only('name', 'price')

    #data = Product.objects.defer('slug') # return all columns with out slug

    #aggregations
    #data = Product.objects.aggregate(Sum('quantity')) # 
    #data = Product.objects.aggregate(Avg('quantity')) # 
    
    # annotate
    #data = Product.objects.annotate(is_new = Value(True)) # 
    data = Product.objects.annotate(price_with_tax = F('price') *1.2) #
    return render(request,'product/debug.html',{'data':data})





# Create your views here.
class ProductList(ListView):
    model = Product

class ProductDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object())
        context["related_products"] = Product.objects.filter(brand=self.get_object().brand)
        return context

class BrandList(ListView):
    model = Brand
    queryset = Brand.objects.annotate(product_count=Count('product_brand'))
    

class BrandDetail(ListView):
    model = Product
    template_name = 'product/brand_detail.html'
    paginate_by = 20

    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        return super().get_queryset().filter(brand=brand)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count('product_brand')) [0]
        return context
    