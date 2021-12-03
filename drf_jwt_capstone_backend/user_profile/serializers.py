from rest_framework import serializers
from django.contrib.auth import get_user_model
User=get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'password', 'email',
                  'first_name', 'last_name', 'state','zip_code','party')
        


        

