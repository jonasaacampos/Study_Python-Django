from django.shortcuts import render, get_object_or_404
from core.models import Produto
from django.http import HttpResponse
from django.template import loader

def index(request):
    #showLogs(request)
    #print(request.user)

    produtos = Produto.objects.all()

    context = { 
        "usuario_logado" : f"{verificaUsuarioLogado(request)}",
        "produtos" : produtos,
    }


    return render(request, "index.html", context)


def contato(request):
    return render(request, "contato.html")


def showLogs(request):
    dict_request_data = request.headers
    print(dict_request_data)   
    for k, v in dict_request_data.items():
        print(f"{k}: {v}")

def verificaUsuarioLogado(request):
    if str(request.user) == "AnonymousUser":
        teste = "Usuário não logado"
    else:
        teste = f"Bem vindo {request.user}!"
    return teste


def produto(request, id):
    #prod = Produto.objects.get(id=id)
    prod = get_object_or_404(Produto,id=id)
    context = {
        "produto" : prod,
    }
    return render(request, "produto.html", context)

def error404(request, e):
    template = loader.get_template("404.html")
    response = HttpResponse(content=template.render(), context_type="text/html; charset=utf8", status=404)
    return response

