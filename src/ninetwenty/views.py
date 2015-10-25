from __future__ import absolute_import

# External Libraries
from django.shortcuts import render
from lindy.models.user import Teacher

def get_context(**context):
    context.update({
        'SITE_NAME': '9:20 Special!',
        'SITE_ROOT': '/920',
    })
    return context


def index(request):
    return render(request, 'landing.jinja2', context=get_context())


def teachers(request):
    context = get_context(
        teachers=Teacher.objects.all().select_related('user')
    )
    return render(request, 'teachers.jinja2', context=context)
