#-*- coding: utf-8 -*-

##################################################
#				DJANGO IMPORTS                   #
##################################################
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import RedirectView, View, UpdateView, ListView, DetailView, DeleteView
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest
from django.forms import formset_factory
from django.db.models import Count, Avg
##################################################


##################################################
#				CUSTOM IMPORTS                   #
##################################################
from .models import *
from .forms import *
import requests
import re
from datetime import datetime
##################################################


class Dashboard(View):
    template_name = "dashboard/dashboard.html"

    def get(self, request):

        obj = Files.objects.all()

        context = {'obj':obj}
        return render(request, self.template_name, context)


def save_files_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            path = request.POST.get('path')
            sub_path = request.POST.get('sub_path')

            obj_sub_path = SubPath.objects.filter(sub_path=sub_path).first()
            if obj_sub_path is None:
                obj_sub_path = SubPath()
                obj_sub_path.sub_path = sub_path
                obj_sub_path.save()

            obj_path = Directories.objects.filter(path=path, sub_path=obj_sub_path).first()
            if obj_path is None:
                obj_path = Directories()
                obj_path.path = path
                obj_path.sub_path = obj_sub_path
                obj_path.save()

            form.path = obj_path
            form.save()

            data['form_is_valid'] = True
            obj = Files.objects.all()
            data['html_list'] = render_to_string('dashboard/modal/list.html', {
                'obj': obj
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def files_create(request):
    if request.method == 'POST':
        form = FilesForm(request.POST, request.FILES)
    else:
        form = FilesForm()
    return save_files_form(request, form, 'dashboard/modal/create.html')


def files_update(request, pk):
    obj = get_object_or_404(Files, pk=pk)
    if request.method == 'POST':
        form = FilesForm(request.POST, request.FILES, instance=obj)
    else:
        form = FilesForm(instance=obj)
    return save_files_form(request, form, 'dashboard/modal/update.html')


def files_delete(request, pk):
    obj = get_object_or_404(Files, pk=pk)
    data = dict()
    if request.method == 'POST':
        obj.delete()
        data['form_is_valid'] = True
        obj = Files.objects.all()
        data['html_list'] = render_to_string('dashboard/modal/list.html', {
            'obj': obj
        })
    else:
        context = {'obj': obj}
        data['html_form'] = render_to_string('dashboard/modal/delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)