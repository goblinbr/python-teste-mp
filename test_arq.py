import unittest
from arq import ArquivoCsv

class TestArquivoCsv(unittest.TestCase):
    def test_init(self):
        arquivoCsv = ArquivoCsv('conteudo.csv')
        self.assertEqual(arquivoCsv.arquivo, 'conteudo.csv')
        self.assertEqual(arquivoCsv.existe, None)

    def test_ler_arquivo_valido(self):
        arquivoCsv = ArquivoCsv('conteudo.csv')
        dados = arquivoCsv.ler()
        self.assertEqual(arquivoCsv.existe, True)
        self.assertEqual(len(dados), 14)
        
        primeiraLinha = dados[0]
        self.assertEqual(primeiraLinha['nome'], 'Diego Faria')
        self.assertEqual(primeiraLinha['cidade'], 'Tubarao')
        self.assertEqual(primeiraLinha['estado'], 'SC')

        ultimaLinha = dados[-1]
        self.assertEqual(ultimaLinha['nome'], 'Gustavo Costa')
        self.assertEqual(ultimaLinha['cidade'], 'Curitiba')
        self.assertEqual(ultimaLinha['estado'], 'PR')

    def test_ler_arquivo_que_nao_existe(self):
        arquivoCsv = ArquivoCsv('conteudox.csv')
        dados = arquivoCsv.ler()
        self.assertEqual(arquivoCsv.existe, False)
        self.assertEqual(len(dados), 0)

    def test_ler_arquivo_vazio(self):
        arquivoCsv = ArquivoCsv('vazio.txt')
        dados = arquivoCsv.ler()
        self.assertEqual(arquivoCsv.existe, True)
        self.assertEqual(len(dados), 0)

if __name__ == '__main__':
    unittest.main()