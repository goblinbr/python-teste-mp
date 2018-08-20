# python-teste-mp

Aplicação desenvolvida em python para ler conteúdo csv ou json  
podendo ser um arquivo local (exemplos: conteudo.csv e conteudo.json) ou uma URL (exemplo: [teste-mp.csv](https://gist.githubusercontent.com/goblinbr/89c3e2dc07187ebbfbdef0485082723e/raw/11fb91cdb30fb98338d8352910f84d71280d4089/teste-mp.csv))

A aplicação agrupa o conteúdo por estado e exibe no terminal a quantidade por estado em ordem alfabética.

- Exemplo:  
\> app.py conteudo.csv  
PR 4  
SC 9  
SP 1  

# Para utilizar sem docker
- Requisito python >= 3.6
- Executar:  
\> app.py arquivo_ou_url


# Rodar os testes
\> python -m unittest