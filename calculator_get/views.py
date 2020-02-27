from django.shortcuts import redirect, render

# Create your views here.

from django.http import HttpResponse

def calc_get(request):
    x = ''
    y = ''
    operation = ''
    result = 0

    if 'plus' in request.GET:

        x = request.GET['number_x']
        y = request.GET['number_y']
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

    elif 'sub' in request.GET:

        x = request.GET['number_x']
        y = request.GET['number_y']
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

    elif 'multi' in request.GET:

        x = request.GET['number_x']
        y = request.GET['number_y']
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


    elif 'div' in request.GET:

        x = request.GET['number_x']
        y = request.GET['number_y']
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

    return render(request, 'calc_get.html', {'x': x, 'y': y, 'result': result,'operation' : operation})
