"""
URL mappings for Recipe API
"""
from django.urls import path, include

from rest_framework.routers import SimpleRouter

from recipe import views


router = SimpleRouter()
router.register(prefix="", viewset=views.RecipeViewSet, basename="recipe")

app_name = "recipe"

urlpatterns = [path("", include(router.urls))]
