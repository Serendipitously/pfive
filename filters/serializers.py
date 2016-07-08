from rest_framework import serializers

from filters.models import Filter, Criteria


class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filter
        fields = ('id', 'name', 'user', 'description',
                  'subscribed', 'criteria')


class CriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criteria
        fields = ('id', 'type', 'query_param', 'weight')
