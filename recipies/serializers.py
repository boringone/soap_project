from rest_framework.serializers import ModelSerializer
from .models import Recipe, Ingredient, Tag


class TagSerializer(ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class IngredientSerializer(ModelSerializer):

    class Meta:
        model = Ingredient
        fields = '__all__'



class RecipiesSerializer(ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)
    ingredients = IngredientSerializer(read_only=True, many=True)
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'tags', 'ingredients']
