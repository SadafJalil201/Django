from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')

def cal(request):
    num1 = int(request.GET.get('num1'))
    num2 = int(request.GET.get('num2'))
    operator = request.GET.get('operator')
    reset = request.GET.get('reset')

    if operator == '+':
        Sum = num1 + num2
        
        result = {'result': Sum}
        return render(request, "index.html", result)
    elif operator == '-':
            Sub = num1 - num2
            result = {'result': Sub}
            return render(request, "index.html", result)
    elif operator == '*':
            Mul = num1 * num2
            result = {'result': Mul}
            return render(request, "index.html", result)
    elif operator == '/':
            Div = num1 / num2
            result = {'result': Div}
            return render(request, "index.html", result)
    else:
        print('value error')
    

        return render(request, "index.html", result)