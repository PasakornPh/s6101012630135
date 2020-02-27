from django.shortcuts import redirect, render

# Create your views here.

from django.http import HttpResponse


def home_page(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def calc_post(request):
    x = ''
    y = ''
    result = 0
    if request.method == 'POST':

        x = request.POST['number_x']
        y = request.POST['number_y']
        print(x,y)

        result = int(x) + int(y)
    return render(request, 'calc_post.html',{'x':x , 'y':y,'result':result})