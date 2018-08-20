import unittest
import os
from internet import baixar_arquivo_temporario, is_url

class TestBaixarArquivoTemporario(unittest.TestCase):
    def test_baixar_arquivo_temporario(self):
        arquivo, status, mensagem = baixar_arquivo_temporario('https://gist.githubusercontent.com/israelbgf/fbdb325cd35bc5b956b2e350d354648a/raw/b26d28f4c01a1ec7298020e88a200d292293ae4b/conteudojson')
        self.assertEqual(status, 200)
        self.assertGreater(os.stat(arquivo).st_size, 0)

    def test_baixar_arquivo_temporario_status_404(self):
        arquivo, status, mensagem = baixar_arquivo_temporario('https://www.google.com/abcdef')
        self.assertEqual(status, 404)
        self.assertEqual(arquivo, None)

    def test_baixar_arquivo_temporario_que_nao_existe(self):
        arquivo, status, mensagem = baixar_arquivo_temporario('http://www.aasodpkaspokdpoasskoaspod.com')
        self.assertEqual(status, -1)
        self.assertEqual(arquivo, None)
        self.assertIn('Erro ao acessar', mensagem)

    def test_is_url(self):
        self.assertEqual(is_url('tex'), False)
        self.assertEqual(is_url('http://www.google.com'), True)
        self.assertEqual(is_url('https://www.google.com'), True)
        self.assertEqual(is_url('https:/www.google.com'), False)
        self.assertEqual(is_url('www.google.com'), False)
        self.assertEqual(is_url('/home/teste'), False)