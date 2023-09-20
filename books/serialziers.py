from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Book, Section


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True, source='section_set.all')

    class Meta:
        model = Book
        fields = '__all__'


class GrantAccessSerializer(serializers.Serializer):
    is_collaborator = serializers.BooleanField(default=False)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='user'
    )
