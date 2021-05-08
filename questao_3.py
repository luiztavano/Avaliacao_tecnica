#importação das bibliotecas
import requests
from bs4 import BeautifulSoup

#url da pagina do login
POST_URL = 'https://nc7-coopertotal.appspot.com'

#informações para o login
payload = {'username': 'leonardo@coopertotal.com.br',
          'password': '1234'}

#url da pagina após o login ser realizado
REQUEST_URL = 'https://nc7-coopertotal.appspot.com/Home'


#criar a session para o login
with requests.Session() as session:
    post = session.post(POST_URL, data=payload)
    r = session.get(REQUEST_URL)

#verificar se página foi carregada com sucesso
print(post)
    
# # r= requests.get('https://quotes.toscrape.com')
# s = BeautifulSoup(r.content, 'html.parser') 
# s_2 = s.find('h5',{'id':'Listar Pedidos'})



# print (r.url)
# print (r.status_code)
# print(s_2)
    

    



    
    




