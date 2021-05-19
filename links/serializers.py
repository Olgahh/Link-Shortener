from rest_framework import serializers
from .models import ShortenLink     
from rest_framework.reverse import reverse


class ShortenLinkSerializer(serializers.ModelSerializer):
    short_link = serializers.SerializerMethodField()
    
    def get_short_link(self, obj):
        # TODO
        request = self.context['request']
        link = reverse("links-detail", args=[obj.link_id], request=request)
        return link

    class Meta:
        model = ShortenLink
        fields = ('full_link', 'link_id', 'short_link')
        read_only_fields = ('link_id',)