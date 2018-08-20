from urllib import request, error
from tempfile import NamedTemporaryFile

def baixar_arquivo_temporario(url):
    nome_do_arquivo = None
    status = None
    mensagem = None
    data = None
    try:
        response = request.urlopen(url)
        data = response.read()
        status = response.status
        response.close()
    except error.HTTPError as e:
        status = e.code
        mensagem = e.reason
    except error.URLError as e:
        status = -1
        mensagem = f'Erro ao acessar {url}\nVerifique se a URL existe e se o acesso a internet está disponível.'

    if status != None and data != None:
        arquivo = NamedTemporaryFile(delete=False)
        nome_do_arquivo = arquivo.name
        arquivo.write(data)
        arquivo.close()

    return nome_do_arquivo, status, mensagem

def is_url(arg):
    return str(arg).startswith('https://') or str(arg).startswith('http://')