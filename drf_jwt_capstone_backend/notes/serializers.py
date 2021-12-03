from rest_framework import serializers
from .models import Notes,Note_Type


class NoteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Notes
        fields = ['note_name', 'note','note_type','user']
        

class NoteTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note_Type
        fields = ['type_name']
        


