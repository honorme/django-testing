from django.http import JsonResponse
from .models import Person
from .serializers import PersonSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def person_list(request):

    if request.method == 'GET':

        # persons = Person.objects.all()
        name = request.GET.get('name')
        description = request.GET.get('description')
        # Filter persons by name or description if the 'name' or 'description' query parameter is provided
        if name:
            persons = Person.objects.filter(name__icontains=name)
        if description:
            persons = Person.objects.filter(description__icontains=description)
        else:
            persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return JsonResponse({'persons': serializer.data})

    if request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def person_detail(request, id):
    try:
        person = Person.objects.get(pk=id)
    except Person.DoesNotExist:
        return JsonResponse({'message': 'The person does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PersonSerializer(person)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        person.delete()
        return JsonResponse({'message': 'The person was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
