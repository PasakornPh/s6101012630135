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
    operation = ''
    result = 0

    if 'plus' in request.POST:

        x = request.POST['number_x']
        y = request.POST['number_y']
        #print(x,y)

        operation = ' + '

        if x == '':
            x = 0
        elif y == '':
            y = 0

        result = float(x) + float(y)
        if str(result).split('.')[1] == '0':
            result = "{:.0f}".format(result)
        else:
            pass

    elif 'sub' in request.POST:

        x = request.POST['number_x']
        y = request.POST['number_y']
        #print(x,y)

        operation = ' - '

        if x == '':
            x = 0
        elif y == '':
            y = 0

        result = float(x) - float(y)
        if str(result).split('.')[1] == '0':
            result = "{:.0f}".format(result)
        else:
            pass

    elif 'multi' in request.POST:

        x = request.POST['number_x']
        y = request.POST['number_y']
        #print(x,y)

        operation = ' * '

        if x == '':
            x = 0
        elif y == '':
            y = 0

        result = float(x) * float(y)
        if str(result).split('.')[1] == '0':
            result = "{:.0f}".format(result)
        else:
            pass


    elif 'div' in request.POST:

        x = request.POST['number_x']
        y = request.POST['number_y']
        #print(x,y)

        operation = ' / '

        if x == '':
            x = 0
        elif y == '':
            y = 0

        result = float(x) / float(y)
        if str(result).split('.')[1] == '0':
            result = "{:.0f}".format(result)
        else:
            pass

    return render(request, 'calc_post.html', {'x': x, 'y': y, 'result': result,'operation' : operation})
