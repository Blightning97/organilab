# encoding: utf-8


'''
Created on 26/12/2016

@author: luisza
'''
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.context import Context
from django.template.loader import get_template
from django.utils import timezone
from django.utils.decorators import method_decorator
from weasyprint import HTML

from laboratory.models import Laboratory, LaboratoryRoom, Object, Furniture
from laboratory.views.djgeneric import ListView


@login_required
def report_labroom_building(request, *args, **kwargs):
    if 'lab_pk' in kwargs:
        rooms = get_object_or_404(
            Laboratory, pk=kwargs.get('lab_pk')).rooms.all()
    else:
        rooms = LaboratoryRoom.objects.all()

    template = get_template('pdf/laboratoryroom_pdf.html')

    context = {
        'object_list': rooms,
        'datetime': timezone.now(),
        'request': request,
        'laboratory': kwargs.get('lab_pk')
    }

    html = template.render(Context(context)).encode("UTF-8")

    page = HTML(string=html, encoding='utf-8').write_pdf()

    response = HttpResponse(page, content_type='application/pdf')
    response[
        'Content-Disposition'] = 'attachment; filename="report_building.pdf"'
    return response


@login_required
def report_objects(request, *args, **kwargs):
    var = request.GET.get('pk')
    if var is None:
        if 'lab_pk' in kwargs:
            objects = Object.objects.filter(
                shelfobject__shelf__furniture__labroom__laboratory__pk=kwargs.get('lab_pk'))
        else:
            objects = Object.objects.all()
    else:
        objects = Object.objects.filter(pk=var)

    template = get_template('pdf/object_pdf.html')

    context = {
        'object_list': objects,
        'datetime': timezone.now(),
        'request': request,
        'laboratory': kwargs.get('lab_pk')
    }

    html = template.render(
        Context(context)).encode("UTF-8")

    page = HTML(string=html, encoding='utf-8').write_pdf()

    response = HttpResponse(page, content_type='application/pdf')
    response[
        'Content-Disposition'] = 'attachment; filename="report_objects.pdf"'
    return response


@login_required
def report_reactive_precursor_objects(request, *args, **kwargs):
    template = get_template('pdf/reactive_precursor_objects_pdf.html')
    lab = kwargs.get('lab_pk')
    if lab:
        rpo = Object.objects.filter(
            shelfobject__shelf__furniture__labroom__laboratory__pk=lab)
    else:
        rpo = Object.objects.all()

    # Reactive precursor objects
    rpo = rpo.filter(type=Object.REACTIVE, is_precursor=True)

    context = {
        'rpo': rpo,
        'datetime': timezone.now(),
        'request': request,
        'laboratory': lab
    }

    html = template.render(Context(context)).encode('UTF-8')

    page = HTML(string=html, encoding='utf-8').write_pdf()

    response = HttpResponse(page, content_type='application/pdf')
    response[
        'Content-Disposition'] = 'attachment; filename="report_reactive_precursor_objects.pdf"'
    return response


@login_required
def report_furniture(request, *args, **kwargs):
    var = request.GET.get('pk')
    lab = kwargs.get('lab_pk')
    if var is None:
        furniture = Furniture.objects.filter(
            labroom__laboratory__pk=lab)
    else:
        furniture = Furniture.objects.filter(pk=var)

    template = get_template('pdf/summaryfurniture_pdf.html')

    context = {
        'object_list': furniture,
        'datetime': timezone.now(),
        'request': request,
        'laboratory': lab
    }

    html = template.render(
        Context(context)).encode("UTF-8")

    page = HTML(string=html, encoding='utf-8').write_pdf()

    response = HttpResponse(page, content_type='application/pdf')
    response[
        'Content-Disposition'] = 'attachment; filename="report_summaryfurniture.pdf"'
    return response


@method_decorator(login_required, name='dispatch')
class ObjectList(ListView):
    model = Object
    template_name = 'laboratory/object_list.html'

    def get_queryset(self):
        query = super(ObjectList, self).get_queryset()
        print(self.lab)
        return query

@method_decorator(login_required, name='dispatch')
class ReactivePrecursorObjectList(ListView):
    model = Object
    template_name = 'laboratory/reactive_precursor_objects_list.html'

    def get_queryset(self):
        query = super(ReactivePrecursorObjectList, self).get_queryset()
        query = query.filter(type=Object.REACTIVE,
                             is_precursor=True,
                             shelfobject__shelf__furniture__labroom__laboratory=self.lab)
        return query