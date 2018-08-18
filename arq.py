import csv

class ArquivoCsv:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.existe = None
    
    def ler(self):
        dados = []
        try:
            with open(self.arquivo) as arq:
                self.existe = True
                leitor = csv.DictReader(arq)
                for linha in leitor:
                    dados.append(linha)
        except FileNotFoundError:
            self.existe = False
        return dados
