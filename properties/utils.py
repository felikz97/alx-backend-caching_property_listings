from django.core.cache import cache
from .models import Property

def get_all_properties():
    properties = cache.get('all_properties')
    if properties is None:
        properties = list(Property.objects.all().values(
            'id', 'title', 'description', 'price', 'location', 'created_at'
        ))
        cache.set('all_properties', properties, 3600)  # Cache for 1 hour
    return properties
def clear_property_cache():
    cache.delete('all_properties')
    # Optionally, you can clear the entire cache if needed
    # cache.clear()