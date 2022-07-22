from django.shortcuts import render
import urllib.request, json 
from urllib.error import HTTPError
from django.http import JsonResponse, HttpResponse
from .models import Endereco


# Create your views here.
def index(request):
    return render(request, 'index.html')

def buscador(cep):
    cep = cep.replace('-','').replace(' ', '').replace('.', '')
    json_cep = 'https://viacep.com.br/ws/' + cep + '/json/'
    with urllib.request.urlopen(json_cep) as url:
        dict_cep = json.loads(url.read().decode())
        output = []
        output.append('CEP: ' + dict_cep['cep'])
        output.append('Logradouro: ' + dict_cep['logradouro'])
        output.append('Bairro: ' + dict_cep['bairro'])
        output.append('Cidade: ' + dict_cep['localidade'])
        output.append('Estado: ' + dict_cep['uf'])
        return '\n\n'.join(output)

def deu_erro(cep):
    cep = cep.replace('-','')
    return False if len(cep) == 8 and cep.isnumeric() else True

def cep_invalido():
    return True

def endereco(request):
    if request.method == 'POST':
        cep = request.POST.get('cep')
    try:
        return render(request, 'endereco.html', {'buscador': buscador(cep)})
    except HTTPError:
        return render(request, 'index.html', {'cep_invalido': cep_invalido()})
    except KeyError:
        return render(request, 'index.html', {'cep_invalido': cep_invalido()})

def api(request, cep):
    endereco = Endereco.objects.filter(cep=cep)
    if not endereco:
        resposta = {
            "erro": "true"
        }
    else:
        resposta = {
            "cep": cep,
            "logradouro": endereco[0].logradouro,
            "bairro": endereco[0].bairro,
            "cidade": endereco[0].cidade,
        }
    return HttpResponse(json.dumps(resposta, ensure_ascii=False, indent=2), content_type="application/json")