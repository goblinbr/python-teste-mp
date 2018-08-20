import sys
from internet import baixar_arquivo_temporario, is_url
from arquivos import ArquivoCsv, ArquivoJson
from agrupamentos import agrupar_dados_por_chave

ATRIBUTO_AGRUPAMENTO = 'estado'

def main():
    arquivo = obter_arquivo_a_partir_dos_parametros()
    dados = obter_dados_arquivo(arquivo, ATRIBUTO_AGRUPAMENTO)
    agrupamento = agrupar_dados_por_chave(dados, ATRIBUTO_AGRUPAMENTO)
    print_agrupamento(agrupamento)

def obter_arquivo_a_partir_dos_parametros():
    parametros = sys.argv[1:]
    if len(parametros) != 1:
        print('Erro: Chamada inválida. Deve receber um parâmetro. Exemplo:\napp.py /home/user/arquivo.csv')
        exit(9)
    
    url_ou_arquivo = parametros[0]
    arquivo = url_ou_arquivo
    if is_url(url_ou_arquivo):
        arquivo, status, mensagem = baixar_arquivo_temporario(url_ou_arquivo)
        if arquivo == None or status == None or status < 200 or status > 299:
            print(f'Erro: {mensagem}')
            if status != None and status > 0:
                print(f'Requisição retornou status: {status}')
            exit(9)
    return arquivo

def obter_dados_arquivo(arquivo, atributo_que_deve_conter):
    arquivoJson = ArquivoJson(arquivo)
    dados = arquivoJson.ler()
    if not arquivoJson.existe:
        print(f'Erro: Arquivo não existe: {arquivo}')
        exit(9)
    if not arquivoJson.valido:
        arquivoCsv = ArquivoCsv(arquivo)
        dados = arquivoCsv.ler()
        if len(dados) <= 0:
            print(f'Erro: Arquivo vazio ou não é um arquivo válido. Deve ser um arquivo json ou csv.')
            exit(9)
        if not atributo_que_deve_conter in dados[0].keys():
            print(f'Erro: Arquivo não contém o atributo {atributo_que_deve_conter}.')
            exit(9)
    return dados

def print_agrupamento(agrupamento):
    for key in sorted(agrupamento.keys()):
        print(key, len(agrupamento[key]))

if __name__ == "__main__":
    main()