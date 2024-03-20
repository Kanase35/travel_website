from django.shortcuts import render
# from django.http import HttpResponse

def calc(request):
    return render(request, 'calc.html', {"name" : "Omkar"})

def add(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    result = val1 + val2 
    return render(request, 'result.html', {"res": result})
