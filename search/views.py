from django.shortcuts import render
from django.http import HttpResponse
from pymongo import cursor, MongoClient
from .models import Search
from django.views.generic import ListView
from django.contrib.messages import constants


def home(request):
    # context = {
    #      'search': Search.objects.all()
    # }
    return render(request, 'search/index.html' )


def details(request):
    query = request.GET['query']
    # allSearch = Search.objects.all()
    allSearch = Search.objects.filter(Old_Catalog__icontains=query)
    # allSearchOld = Search.objects.filter(Old_Catalog__icontains=query)
    # allSearchNew = Search.objects.filter(Final_Catalog__icontains=query)
    # allSearch = allSearchOld.union(allSearchNew, all=True)

    params = {'allSearch': allSearch, 'query': query}
    return render(request, 'search/details.html', params)












