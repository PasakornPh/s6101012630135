from django.shortcuts import redirect, render
from calculator.models import saveResult
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
    x_input = ''

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

        save_value = saveResult(val_results=result)
        save_value.save()

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

        save_value = saveResult(val_results=result)
        save_value.save()

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

        save_value = saveResult(val_results=result)
        save_value.save()


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

        save_value = saveResult(val_results=result)
        save_value.save()

    elif 'continue' in request.POST:
        show_history = saveResult.objects.all()
        x_last = str(show_history.last())

        print(x_last.split('.'))

        if x_last.split('.')[1] == '0':
            x_last = x_last.split('.')[0]
        else:
            pass

        x_input = int(x_last)

        print(x_input)

    return render(request, 'calc_post.html', {'x': x, 'y': y, 'result': result,'operation' : operation,'x_input':x_input})

