from rest_framework import viewsets
from django.http import HttpResponseRedirect
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from django.shortcuts import get_object_or_404

from .models import ShortenLink
from .serializers import ShortenLinkSerializer


class ShortenLinkViewSet(ListModelMixin, RetrieveModelMixin, CreateModelMixin, 
                DestroyModelMixin, UpdateModelMixin, viewsets.GenericViewSet):

    queryset = ShortenLink.objects.all()
    serializer_class = ShortenLinkSerializer
    lookup_field = 'link_id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        return HttpResponseRedirect(redirect_to=instance.full_link)

            




