from django.shortcuts import render
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
# Create your views here.
from .models import Listing


def index(request):

    listings  =  Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 1)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/index.html', context)


def search(request):
    return render(request, 'listings/search.html')


def listing(request):
    return render(request, 'listings/listing.html')