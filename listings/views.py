from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator
from .choices import state_choices, bedroom_choices, price_choices


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)
    page_number = request.GET.get('page')
    paged_listings = paginator.get_page(page_number)
    context = {'listings': paged_listings}
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing_obj = get_object_or_404(Listing, pk=listing_id)
    context = {'listing': listing_obj}
    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.all().order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    context = {
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'listings': queryset_list
    }
    return render(request, 'listings/search.html', context)
