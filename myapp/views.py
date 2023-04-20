from django.shortcuts import render

# Create your views here.
def background(request):
    return render(request, 'backgroundimages.html')

def images(request):
    return render(request, 'images.html')

def imagetext(request):
    return render(request, 'imagetext.html')

def form(request):
    return render(request, 'form.html')