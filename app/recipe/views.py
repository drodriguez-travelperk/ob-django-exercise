"""
Views for Recipe APIs
"""
from rest_framework import viewsets

from core.models import Recipe
from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    """View for manage recipe apis"""

    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()

    def get_queryset(self):
        """Retrieve list of recipes"""
        return self.queryset.order_by("-name")
