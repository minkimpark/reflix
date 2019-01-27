#-*- coding: utf-8 -*-
import os
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt

def test(request):
    print('-------def test')
    return render(request,'test/test.html')
