
def agrupar_dados_por_chave(dados, chave):
    agrupamento = {}
    for d in dados:
        valor_chave = d[chave]
        lista = agrupamento.get(valor_chave, [])
        if len(lista) == 0:
            agrupamento[valor_chave] = lista
        lista.append(d)
    return agrupamento