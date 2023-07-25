from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
# Create your views here.
def homeView(request):
    return JsonResponse({"message": "good luck"})