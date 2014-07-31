from django.shortcuts import render

# Create your views here.
from forms import *


def home(request):
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()
            return render(request, "home.html", photo)
    else:
        form = PhotoForm()
    data = {"form": form}
    return render(request, "home.html", data)



def profile_update(request):
    user = User.objects.get(id=user_id)
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UserForm(instance=user)
    data = {"user": request.user, "form": form}
    return render(request, "profile/profile_update.html", data)

