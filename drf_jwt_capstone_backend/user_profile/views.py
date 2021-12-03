from functools import partial
from django.http.response import Http404
from django.contrib.auth import get_user_model
User=get_user_model()
from .serializers import ProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  status
from rest_framework.permissions import IsAuthenticated


class Profile(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self,request, pk ):
        Profile = self.get_object(pk)
        serializer = ProfileSerializer(Profile)
        return Response(serializer.data)

    def put(self,request,pk):
        Note = self.get_object(pk)
        serializer = ProfileSerializer(Note, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        Profile = self.get_object(pk)
        Profile.delete()
        return Response(status=status.HTTP_200_OK)