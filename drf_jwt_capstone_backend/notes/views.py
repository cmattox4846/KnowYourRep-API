from functools import partial
from django.http.response import Http404
from .models import Note_Type, Notes
from .serializers import NoteSerializer, NoteTypeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  status
import time
from rest_framework.permissions import IsAuthenticated


class NoteList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        time.sleep(0.5)
        Note = Notes.objects.all()
        serializer = NoteSerializer(Note, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NoteDetails(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self,pk):
        try:
            return Notes.objects.get(pk=pk)
        except Notes.DoesNotExist:
            raise Http404
   
    def get(self,request, pk ):
        Note = self.get_object(pk)
        serializer = NoteSerializer(Note)
        return Response(serializer.data)

    def put(self,request,pk):
        Note = self.get_object(pk)
        serializer = NoteSerializer(Note, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        Note = self.get_object(pk)
        Note.delete()
        return Response(status=status.HTTP_200_OK)

class NoteTypeList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        time.sleep(0.5)
        Note = Note_Type.objects.all()
        serializer = NoteTypeSerializer(Note, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = NoteTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



       
