#Importação da biblioteca
import scrapy

class Compra_agora_spider(scrapy.Spider):
    name = 'compra-agora'
    start_urls = ['https://www.compra-agora.com/']
    
    #método para pegar a url de cada categoria de produtos
    def parse(self, response):    
    
        self.lista_url =[]
        categorias = response.css('div.titulo-subcategorias.ver-tudo')
        for itens in categorias:
            self.lista_url.append(itens.css('a.menu-text::attr(href)').get())
        
        #chamar o método para extrair todas as url's da primeira categoria de produtos
        self.i = 0
        yield scrapy.Request(
                url=response.urljoin(self.lista_url[self.i]),
                callback=self.paginacao)
    
    #método para pegar todas as url's presente na categoria de produtos
    def paginacao (self, response):
        
        #pegar o nome da categoria de produtos
        categoria = response.css('div.breadcrumbs-mobile ul li.breadcrumbs-itens.breadcrumbs-itens-escuro p::text').get()
        yield {'Capturando Produtos da categoria': categoria}
        
        #pegar o número da última página
        ultima_pagina = response.css('div.busca-paginacao div div div a.ultima ::attr(data-pagina)').get()
        
        #Criar uma lista para armazenar todas as url's
        self.lista_todas_url = []
        self.lista_todas_url.append(self.lista_url[self.i])
        
        #loop para pegar todas as url's
        for self.j in range(2, int(ultima_pagina)+1):        
            proxima_url = self.lista_url[self.i] + "?p=" + str(self.j) + "&amp;ordenacao=0&amp;limit=24&amp;ajaxScroll=1"        
            self.lista_todas_url.append(proxima_url)    

        #chamar o método para realizar a extração do conteúdo da primeira página        
        self.j = 0    
        yield scrapy.Request(
                url=response.urljoin(self.lista_todas_url[self.j]),
                callback=self.pagina, dont_filter = True)
        
    #método para extração do conteúdo
    def pagina(self, response): 
        
        #pegar as informações da div Produtos
        produtos = response.css('div#divProdutos ul li')
                
        #loop para extrair as informaçoes dos produtos
        for produto in produtos:
            
            descricao = produto.css('div div div a div figure img::attr(alt)').extract()
            imagem_url = produto.css('div div div a div figure img::attr(src)').extract()
            
            yield {'descricao': descricao[0],
                   'descricao_fabricante': produto.css('div div div div div div div a.produto-marca.mb-1::text').get(),
                   'imagem_url':imagem_url[1]}
        
        #determinar a qual próximo método será chamado
        #se ainda houver url na atual categoria de produtos, chamar a próxima url
        if self.j < (len(self.lista_todas_url)-1):
             self.j = self.j + 1
             yield scrapy.Request(
                url=response.urljoin(self.lista_todas_url[self.j]),
                callback=self.pagina, dont_filter = True)    
        
        #se todas as url's já tiverem sido raspadas, chamar a próxima categoria de produtos
        elif self.i < (len(self.lista_url)-1):
            self.i = self.i + 1
            yield scrapy.Request(
                url=response.urljoin(self.lista_url[self.i]),
                callback=self.paginacao)
        
        
    
            
