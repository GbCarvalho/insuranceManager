from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Policy
from .serializer import PolicySerializer

# Create your views here.


@api_view(['GET'])
def policy_list(request):
    if request.method == 'GET':
        queryset = Policy.objects.all()
        serializer = PolicySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer_class.data, status=status.HTTP_200_OK)
