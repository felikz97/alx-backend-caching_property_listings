from django.shortcuts import render

# Create your views here.

from django.views.decorators.cache import cache_page
from .models import Property

@cache_page(60 * 15)  # Cache for 15 minutes
def property_list(request):
    properties = Property.objects.all()
    return render(request, 'properties/property_list.html', {'properties': properties})
