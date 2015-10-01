from django.shortcuts import render


context = {
    'SITE_NAME': '9:20 Special!'
}


# Create your views here.
def index(request):
    return render(request, 'landing.jinja2', context=context)
