import requests
import re
from bs4 import BeautifulSoup

pesquisa = input("Digite O Que Você Quer Pesquisar: ")

url = f'https://www.google.com/search?q={pesquisa}&sca_esv=587264773&tbm=shop&source=lnms&sa=X&ved=2ahUKEwi5y4Kp0fCCAxVCqpUCHQ6KB0YQ_AUoAXoECAIQAw&biw=1242&bih=619&dpr=1.1&gl=BR'

resposta = requests.get(url)
soup = BeautifulSoup(resposta.content, 'html.parser')

primeiro_produto= soup.find(id="rmenu").find_next_siblings('div')[1] ## Pega a Próxima tag
# Depois de 'rdmenu', e o '1' vai ser a outra próxima div

classe_produto = primeiro_produto.get('class')[0] 
# Depois pega a class desse elemento, pois as classes dos produtos são as mesmas

produtos = soup.findAll('div', { "class": classe_produto })
# Procura todas as tags div com a mesma classe que a tag anterior

'''
def importar(): 
        with open('pg.html', 'w', encoding='utf-8') as file:
            file.write(str(resposta.content))
        print("Código HTML escrito com sucesso e salvo como 'pg.html'")

importar()  
'''

lista = {}
lista2 = []
remover = ''
menor = 9999999.99
menores = []

for produto in produtos[:-3]:
    nome = produto.findChildren()[0].findChildren()[6].getText()
    preco = produto.findChildren()[0].findChildren()[-2].getText()
    link = produto.findChildren()[0].findChildren()[6].get('href')

    lista[nome] = preco
    

    print(nome)
    print("=============================")
    print(preco)
    print("\n Link:")
    print(link)
    print("\n\n")

    # SE O VALOR NO DICIONÁRIO ESTIVER VAZIO NÃO PODE SER ADICIONADO

for chave, valor in lista.items():
    resultado_busca = re.search(r'\d[\d.,]*', valor)
    if resultado_busca:
        apenas_numeros = resultado_busca.group()
        apenas_numeros = float(apenas_numeros.replace('.', '').replace(',', '.'))

        #print(f"Produto: \n {chave} \n Preço: {apenas_numeros} \n  =========== \n", type(apenas_numeros))
        #lista2[chave] = apenas_numeros
        lista2.append(apenas_numeros)
        #print(lista2)
            
    else:
        remover = chave
        print(f"Chave {chave}: Números não encontrados na string")

lista.pop(remover)
lista2 = sorted(lista2)
lista2.reverse()

for i in range(-10, 0, 1):
    menor = lista2[-1]
    menores.append(lista2[i])
    
    
    #print(f'\n \n {menor}, {menores}')

#print('\n |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||', '\n \n')
#print('O Produto mais barato é: ', menor, '\n')
print('TOP - 10 \n ')
print(' -', lista2[-1], '\n')
print(' -', lista2[-2], '\n')
print(' -', lista2[-3], '\n')
print(' -', lista2[-4], '\n')
print(' -', lista2[-5], '\n')
print(' -', lista2[-6], '\n')
print(' -', lista2[-7], '\n')
print(' -', lista2[-8], '\n')
print(' -', lista2[-9], '\n')
print(' -', lista2[-10], '\n')

lista2 = lista.items() # Adicionar uma lista pra ir removendo e ir deixando nos top 10 minimos

#print(list(lista.items()))
