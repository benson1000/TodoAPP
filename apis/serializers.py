from rest_framework import serializers
from todo.models import Todo


#ModelSerializer provides an API to create serializers from your models.
class TodoSerializer(serializers.ModelSerializer):
    created_at = serializers.ReadOnlyField()
    completed = serializers.ReadOnlyField()


    class Meta:
        model = Todo  #the database model
        fields = ["id", "title","memo", "created_at", "completed"]   # the fields to expose.


class TodoToggleCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id"]
        read_only = ["title", "memo", "created_at", "completed"]