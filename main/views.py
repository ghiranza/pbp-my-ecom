from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'free 500 v-bucks',
        'price': 'Rp20.000',
        'deskripsi': 'you will get 500 v-bucks with extra 100',
        'bonus':'100',
    }

    return render(request, "main.html", context)