from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . serializers import *

from django.http import JsonResponse

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/<id>/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/<id>/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/<id>/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing note'
        },
    ]

    return Response(routes)

@api_view(['GET', 'POST'])
def getNotes(request):
    if (request.method == 'GET'):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    elif (request.method == 'POST'):
        data = request.data
        note = Note.objects.create(body=data['body'])
        serializer = NoteSerializer(note, many=False)
        return Response(serializer.data)
    else:
        return Response("No action for this request method")

@api_view(['GET', 'PUT', 'DELETE'])
def crudNote(request, pk):
    if (request.method == 'GET'):
        note = get_object_or_404(Note, id=pk)
        serializer = NoteSerializer(note, many=False)
        return Response(serializer.data)
    elif (request.method == 'PUT'):
        data = request.data
        note = get_object_or_404(Note, id=pk)
        serializer = NoteSerializer(instance=note, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("Something went wrong")
    elif (request.method == 'DELETE'):
        note = get_object_or_404(Note, id=pk)
        note.delete()
        return Response('Note was deleted')
    else:
        return Response("No action for this request method")