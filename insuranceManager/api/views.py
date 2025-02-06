from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Policy
from .serializer import PolicySerializer

# Create your views here.


@api_view(['GET', 'POST'])
def policy_list(request):
    if request.method == 'GET':
        queryset = Policy.objects.all()
        serializer = PolicySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = PolicySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def policy_details(request, pk):
    try:
        policy = Policy.objects.get(pk=pk)
    except Policy.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer_class = PolicySerializer(policy)
        return Response(serializer_class.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer_class = PolicySerializer(policy, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_200_OK)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
