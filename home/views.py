from django.shortcuts import render

# Create your views here.

from home.models import CustomText, HomePage


def home(request):
    packages = [
	{'name':'django-shop', 'url': 'http://pypi.python.org/pypi/django-shop/0.11.3'},
	{'name':'django-social-auth', 'url': 'http://pypi.python.org/pypi/django-social-auth/0.7.28'},
    ]
    context = {
        'customtext': CustomText.objects.first(),
        'homepage': HomePage.objects.first(),
        'packages': packages
    }
    return render(request, 'home/index.html', context)
