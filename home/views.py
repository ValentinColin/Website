import typing
from django.shortcuts import render
from dotmap import DotMap
from home.context import hydrate, home_context

DOTMAP = typing.TypeVar('DotMap', bound=typing.OrderedDict)

# Exemple
# from django.http import HttpResponse
# def index(request):
#     return HttpResponse("Hello, world. You're at the home index.")


@hydrate(home_context)
def home(request, context: DOTMAP = DotMap({})):
    return render(request, "home/home.html", context)