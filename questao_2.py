#importação da biblioteca
import scrapy
from scrapy.exceptions import CloseSpider
 
class Pedido_Servimed_Spider(scrapy.Spider):
    name = 'Pedido_servimed'
    start_urls = ['https://pedidoeletronico.servimed.com.br/login']

    #método para realizar o login
    def parse(self, response):

        yield scrapy.FormRequest(
            url='https://pedidoeletronico.servimed.com.br/login',
            formdata={
                'username': 'juliano@farmaprevonline.com.br',
                'password': 'a007299A'},
            callback=self.parse_menu,
        )

    #método para abrir a página de menu 
    def parse_menu(self, response):
        has_logout_link = response.url
        if not has_logout_link:
            raise CloseSpider('não deu certo')
            
        self.log('acabei de fazer login')
        self.log(has_logout_link)
        
        yield scrapy.Request(
            url=response.urljoin('https://pedidoeletronico.servimed.com.br/'),
            callback=self.menu)
    
    #método para abrir a página de pedidos
    def menu(self, response):
        self.log(response.url)
        link = response.css('body app-root')
        yield  {'valor':link}        
 