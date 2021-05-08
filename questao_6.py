#importação das bibliotecas
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def scraping_selenium(author_name):

    #caminho aonde está salvo o chromedriver
    # DRIVER_PATH = 'C:/Users/tavan/OneDrive/Documentos/chromedriver.exe'
    DRIVER_PATH = 'C:/Users/DBI5/Documents/chromedriver.exe'
    
    #passar opções
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    
    #Pegar informações da página
    driver.get("https://quotes.toscrape.com/")
    
    #Pegar citação referente ao nome do autor
    quotes = driver.find_element_by_xpath("//*[contains(text(), '" + author_name + "')]/ancestor::div[1]")
    
    #Pegar o link para informações sobre o autor
    about= quotes.find_elements_by_tag_name('a')
    link = about[0].get_attribute('href')
    driver.get(link)
    
    #Pegar informações sobre o autor
    born = driver.find_elements_by_class_name('author-born-date')
    location = driver.find_elements_by_class_name('author-born-location')
    description = driver.find_elements_by_class_name('author-description')
    
    #criar dicionários para armazenar as informações
    extract ={}
    author = {}
    
    author["name:"] = author_name
    author["birth_date:"] = born[0].text
    author["birth_location:"] = location[0].text
    author["description:"] = description[0].text
    
    extract["author:"] = author
    
    #voltar para a página inicial
    next_page = "https://quotes.toscrape.com/"  
    driver.get(next_page)
    class_next_page = 1
    
    #loop para extrair informações de cada página
    lista = []
    while class_next_page != []:
        
        #pegar link da próxima página
        class_next_page = driver.find_elements_by_class_name('next')
        
        #tentar executar
        try:
            
            #pegar informações pelo nome da classe
            quotes = driver.find_elements_by_class_name('quote')
    
            #loop para verificar se as citações são do autor procurado
            for i in range(len(quotes)):
                
                #Pegar nome do autor de cada citação da página
                author= quotes[i].find_elements_by_class_name('author')
                
                #verificar se o autor da citação é autor procurado
                if author[0].text == author_name:
                    
                    #Caso seja, pegar a citação
                    quote = quotes[i].find_elements_by_class_name('text')
                    quote_text = quote[0].text
                
                    #Pegar tags da citação
                    tags = quotes[i].find_elements_by_class_name('tag')
                    lista_tag = []
                    for j in range(len(tags)):
                        tag = tags[j].text
                        lista_tag.append(tag)
                    
                    #Criar lista de dicionários com as informações coletadas
                    content = {"text" : quote_text, "tags" : lista_tag}
                    lista.append(content)
    
            #Pegar link da próxima página
            a_next_page = class_next_page[0].find_elements_by_tag_name("a")
            next_page = a_next_page[0].get_attribute('href')
            driver.get(next_page)
        
        except:
            class_next_page = []
    
    #Adicionar informações extraídas no dicionário
    extract["quotes"] = lista
    
    #Fechar conexão com a página
    driver.quit() 
        
    return extract 

author = 'J.K. Rowling'
extracao = scraping_selenium(author)

print(extracao)
