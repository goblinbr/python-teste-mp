from csv import DictReader
import json

class ArquivoCsv:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.existe = None
    
    def ler(self):
        dados = []
        try:
            with open(self.arquivo, encoding='utf-8') as arq:
                self.existe = True
                leitor = DictReader(arq)
                for linha in leitor:
                    dados.append(linha)
        except FileNotFoundError:
            self.existe = False
        return dados

class ArquivoJson:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.existe = None
        self.valido = None
    
    def ler(self):
        dados = []
        try:
            with open(self.arquivo, encoding='utf-8') as arq:
                self.existe = True
                dados = json.load(arq)
                self.valido = True
        except FileNotFoundError:
            self.existe = False
            self.valido = False
        except json.decoder.JSONDecodeError:
            self.valido = False
        return dados