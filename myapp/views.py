
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to conditions")


def biggest(request):
    a = 10
    b = 20
    c = 15

    biggest_num = max(a, b, c)

    return HttpResponse(f"biggest of 3 numbers is {biggest_num}")


def smallest(request):
    a = 10
    b = 20
    c = 15

    smallest_num = min(a, b, c)

    return HttpResponse(f"smallest of 3 numbers is {smallest_num}")


def even(request):
    num = 8

    if num % 2 == 0:
        return HttpResponse(f"yes, {num} is even number")
    else:
        return HttpResponse(f"no, {num} is not even number")


def odd(request):
    num = 7

    if num % 2 != 0:
        return HttpResponse(f"yes, {num} is odd number")
    else:
        return HttpResponse(f"no, {num} is not odd number")