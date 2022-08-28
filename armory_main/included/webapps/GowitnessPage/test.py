from django.shortcuts import render
from django.http import HttpResponse
from armory2.armory_main.models import *
from django.shortcuts import render, get_object_or_404
from django.template.defaulttags import register
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from pathlib import Path
from base64 import b64encode
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


ips = IPAddress.objects.all()
domains = Domain.objects.all()
print("hello world")
print(ips[0].port_set.all())
print(domains)