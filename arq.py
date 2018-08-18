from csv import DictReader

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
