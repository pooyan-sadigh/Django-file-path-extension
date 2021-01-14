from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Product


# Create your views here.

# CBV LISTVIEW
class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/product_list.html"

# CBV DETAILVIEW
class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/product_detail.html"
