from django.shortcuts import render, redirect
from main.forms import VBucksEntryForm
from main.models import VBucksEntry
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    vbucks_entries = VBucksEntry.objects.all()

    context = {
        'name' : '500 V-Bucks',
        'price': 'Rp20.000',
        'description': 'you will get 500 v-bucks with extra 100',
        'bonus':'+100',
        'vbucks_entries': vbucks_entries
    }

    return render(request, "main.html", context)

def create_vbucks_entry(request):
    form = VBucksEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
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