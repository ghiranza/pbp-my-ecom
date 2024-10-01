from django.shortcuts import render, redirect, reverse
from main.forms import VBucksEntryForm
from main.models import VBucksEntry
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    vbucks_entries = VBucksEntry.objects.filter(user=request.user)

    last_login = request.COOKIES.get('last_login', 'Belum ada data login')

    context = {
        'name' : request.user.username,
        'npm' : '2306165944',
        'class' : 'PBP B',
        # 'price': 'Rp20.000',
        # 'description': 'you will get 500 v-bucks with extra 100',
        # 'bonus':'+100',
        'vbucks_entries': vbucks_entries,
        'last_login': last_login,
    }

    return render(request, "main.html", context)

def create_vbucks_entry(request):
    form = VBucksEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        vbucks_entry = form.save(commit=False)
        vbucks_entry.user = request.user
        vbucks_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_vbucks_entry.html", context)

def show_xml(request):
    data = VBucksEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = VBucksEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = VBucksEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = VBucksEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_vbucks(request, id):
    # Get vbucks entry berdasarkan id
    vbucks = VBucksEntry.objects.get(pk = id)

    # Set vbucks entry sebagai instance dari form
    form = VBucksEntryForm(request.POST or None, instance=vbucks)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_vbucks.html", context)

def delete_vbucks(request, id):
    # Get vbucks berdasarkan id
    vbucks = VBucksEntry.objects.get(pk = id)
    # Hapus vbucks
    vbucks.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))