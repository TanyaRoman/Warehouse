from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404


def tab_list_view(request, *args, **kwargs):
    return render(request, "home.html")
