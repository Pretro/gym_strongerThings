from django.shortcuts import get_object_or_404, render
from .models import Product
from django.views.generic.detail import DetailView
from django.db.models import Q


# Create your views here.
def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(
        Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'products/products.html', {'products': products, 'query': query})


class ProductDetailView(DetailView):

    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contador'] = 100
        return context


def all_products(request):

    products = Product.objects.all()

    context = {
        'products': products,

    }

    return render(request, 'products/products.html', context)
