from rest_framework import viewsets
from rest_framework import filters

from neodoli.models import Place
from .serializers import PlaceSerializer

class PharmacyViewSet(viewsets.ReadOnlyModelViewSet):

	queryset = Place.objects.filter(category='ph')
	serializer_class = PlaceSerializer
	filter_backends = (filters.SearchFilter,)
	search_fields = ('name', 'city', 'address', 'email',)


class ClinicViewSet(viewsets.ReadOnlyModelViewSet):

	queryset = Place.objects.filter(category='cli')
	serializer_class = PlaceSerializer
	filter_backends = (filters.SearchFilter,)
	search_fields = ('name', 'city', 'address', 'email',)


class LaboratoryViewSet(viewsets.ReadOnlyModelViewSet):

	queryset = Place.objects.filter(category='lab')
	serializer_class = PlaceSerializer
	filter_backends = (filters.SearchFilter,)
	search_fields = ('name', 'city', 'address', 'email',)