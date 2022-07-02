from django.shortcuts import render, HttpResponse


# Create your views here.

def hello(request):
    return HttpResponse('<h1>Hello World!</h1>')


def user_data_processing(request, name, age, nationality):
    return HttpResponse(
        f'<h1>Dados do Usuário</h1><h2>Nome: {name}</h2><h2>Idade: {age} anos</h2><h2> Nacionalidade: {nationality}')


def sum(request, number1, number2):
    resultado = number1 + number2
    return HttpResponse('<h1>Resultado da soma:<h1><h2>{} + {} = {}</h2>'.format(number1, number2, resultado))


def subtraction(request, number1, number2):
    resultado = number1 - number2
    return HttpResponse('<h1>Resultado da subtração:<h1><h2>{} - {} = {}</h2>'.format(number1, number2, resultado))


def multiplication(request, number1, number2):
    resultado = number1 * number2
    return HttpResponse('<h1>Resultado da multiplicação:<h1><h2>{} * {} = {}</h2>'.format(number1, number2, resultado))


def division(request, number1, number2):
    resultado = number1 / number2
    return HttpResponse('<h1>Resultado da divisão:<h1><h2>{} / {} = {}</h2>'.format(number1, number2, resultado))
