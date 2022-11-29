from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Recipe, Ingredient, Tag
from .serializers import RecipiesSerializer

# Create your views here.

@api_view(['GET'])
def get_routes(request):
    return Response([{"ENDPOINT": "asdasdd"}])

@api_view(['GET'])
def get_recipies(request):
    all_recipies = Recipe.objects.all()
    recipies_serializer = RecipiesSerializer(all_recipies, many=True)
    return Response(recipies_serializer.data)

@api_view(['GET'])
def get_recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    recipe_serializer = RecipiesSerializer(recipe, many=False)
    return Response(recipe_serializer.data)
