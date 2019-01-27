#-*- coding: utf-8 -*-
import os
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt

def test_view(request):
    print('coming')
    search_keyword = request.GET.get('search_keyword')
    context = {}
    context['search_keyword'] = search_keyword
    print(search_keyword)
    return render(request,'test/test_view.html',context)
