from django.shortcuts import render

# Create your views here.

def site_a(request):
    return render(request,'indexa.html')