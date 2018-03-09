from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
import datetime
import json

def index(request):
	return render(request, 'ResumeSite/index.html')