from rest_framework import serializers
from django.utils.html import escape
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id","title","content","created_at","updated_at"]
        read_only_fields = ["id","created_at","updated_at"]


    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Note title is required")
        return escape(value.strip())

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("Note content is required")
        return escape(value.strip())

class NoteCreateSerializer(NoteSerializer):
    pass



class NoteUpdateSerializer(serializers.ModelSerializer):
    # ОБНОВДЕНИЕ КОНТЕТА
    title = serializers.CharField(required=False)
    content = serializers.CharField(required=False)
