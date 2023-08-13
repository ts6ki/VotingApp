from django.shortcuts import render

from support import SupportDepartment, Ticket

def openTicket(request):
    department = SupportDepartment.objects.all()
    if request.method == "POST":
        c = Ticket()
        c.name = request.POST.get("name")
        c.email = request.POST.get("email")
        c.content = request.POST.get("content")
        c.department_id = request.POST.get("department")
        c.save()
    return render(request, "general/contactus.html", {"departments": SupportDepartment})

