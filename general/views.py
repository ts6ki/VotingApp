from django.http import HttpResponse


def contact_us(request):
    return HttpResponse("Contact us here")

def about_us(request):
    return HttpResponse("Who we are")

def about_us_detailed(request, username):
    return HttpResponse("Who is " + username + "?")
