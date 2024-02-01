from django.shortcuts import redirect, render
from requests import request
from .models import Usercrud
# Create your views here.

def home(request) :
    return render(request , "home.html")

def crud(request) :
    return render(request , "user.html")

from django.shortcuts import render, redirect
from .models import Usercrud

def insertuser(request):
    vid = request.POST['ID']
    vname = request.POST['name']
    vemail = request.POST['email']
    vbranch = request.POST['branch']
    if 'image' in request.FILES:
        vimage = request.FILES['image']
    else:
        vimage = None  # or handle it as per your application logic

    # Create a new Usercrud instance with the provided data
    us = Usercrud(uid=vid, name=vname, email=vemail, branch=vbranch, image=vimage)
    us.save()

    return render(request, "home.html")


def show(request):
    users=Usercrud.objects.all()
    return render(request ,"show.html",{'users':users})

def delete(request,uid):
    user=Usercrud.objects.get(uid=uid)
    user.delete()
    return redirect('/show')

def edit(request,uid):
    user=Usercrud.objects.get(uid=uid)
    return render(request,'edit.html',{'user':user})

from django.shortcuts import render, redirect
from .models import Usercrud

def update(request, uid):
    if request.method == 'POST':
        # Assuming you have a form with fields 'ID', 'name', 'email', 'branch', 'image'
        vid = request.POST['ID']
        vname = request.POST['name']
        vemail = request.POST['email']
        vbranch = request.POST['branch']

        # Get the Usercrud object to update
        user = Usercrud.objects.get(uid=uid)

        # Update the fields
        user.uid = vid
        user.name = vname
        user.email = vemail
        user.branch = vbranch

        # Check if a new image is provided in the request
        if 'image' in request.FILES:
            vimage = request.FILES['image']
            user.image = vimage

        # Check if the user wants to remove the existing image
        if 'remove_image' in request.POST:
            user.image.delete()  # Delete the existing image

        # Save the updated object
        user.save()

        return redirect('/show')

    else:
        # If the request method is not POST, render the edit form
        user = Usercrud.objects.get(uid=uid)
        return render(request, 'edit.html', {'user': user})