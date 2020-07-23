from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from board.models import PriceBySize


def get(request):

    return JsonResponse({'result': 'SUCCESS'}, status=200)
