import unittest
from agrupamentos import agrupar_dados_por_chave

class TestAgrupamentos(unittest.TestCase):
    def test_agrupar_dados_por_chave_com_lista_vazia(self):
        dados = []
        agrupamento = agrupar_dados_por_chave(dados, '')
        self.assertEqual(len(agrupamento), 0)

    def test_agrupar_dados_por_chave_com_um_elemento(self):
        dados = [{ 'nome': 'John Wick', 'cidade': 'Tubarão', 'estado': 'SC' }]
        agrupamento = agrupar_dados_por_chave(dados, 'estado')
        self.assertEqual(len(agrupamento), 1)
        self.assertEqual(len(agrupamento['SC']), 1)
        self.assertEqual(agrupamento['SC'][0], dados[0])

    def test_agrupar_dados_por_chave_com_mais_elemento(self):
        estados = { 'SC': 10, 'SP': 37, 'MG': 40 }
        dados = []
        for estado in estados.keys():
            for i in range(estados[estado]):
                dados.append({ 'nome': f'Nome {i}', 'cidade': f'cidade de {estado} {i}', 'estado': estado })
        agrupamento = agrupar_dados_por_chave(dados, 'estado')
        self.assertEqual(len(agrupamento), len(estados))
        self.assertEqual(len(agrupamento['SC']), estados['SC'])
        self.assertEqual(len(agrupamento['SP']), estados['SP'])
        self.assertEqual(len(agrupamento['MG']), estados['MG'])