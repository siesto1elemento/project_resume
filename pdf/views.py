from django.shortcuts import render
from .models import Profile
# Create your views here.


def accept(request):
    if request.method == "POST":
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        phone = request.POST.get("phone","")

        profile = Profile(name=name,email=email,phone=phone)
        profile.save()

    return render(request,'pdf/accept.html')