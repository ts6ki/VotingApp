from django.http import HttpResponse
from django.shortcuts import render

from general.models import ContactUs, Department


def contact_us(request):
    departments = Department.objects.all()
    if request.method == "POST":
        c = ContactUs()
        c.name = request.POST.get("name")
        c.email = request.POST.get("email")
        c.content = request.POST.get("content")
        c.department_id = request.POST.get("department")
        c.save()
    return render(request, "general/contactus.html", {"departments": departments})

def about_us(request):
    return HttpResponse("Who we are")

def about_us_detailed(request, username):
    return HttpResponse("Who is " + username + "?")
