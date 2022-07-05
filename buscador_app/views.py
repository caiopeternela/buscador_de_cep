from django.shortcuts import render
import urllib.request, json 


# Create your views here.
def index(request):
    return render(request, 'index.html')

def buscador(cep):
    cep = cep.replace('-','')
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
        
def endereco(request):
    if request.method == 'POST':
        cep = request.POST.get('cep')
    return render(request, 'endereco.html', {'buscador': buscador(cep)})