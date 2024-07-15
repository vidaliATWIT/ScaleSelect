from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import getScale, getKey


@api_view(['GET'])
def generate_scale(request):
    scale = getScale()
    key = getKey()
    return Response({'message': key + ' ' + scale})