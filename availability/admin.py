from django.contrib.contenttypes.generic import GenericStackedInline
from .models import Availability

class AvailabilityStackedInline(GenericStackedInline):
    model = Availability
    extra = 2
