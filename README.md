# Avaliacao Técnica
Repositório contendo os scripts solicitados na Avaliação Técnica

## Questão 1
O presente script tem como objetivo realizar o login no site [compra-agora.com](https://www.compra-agora.com/) e a extração de informações dos produtos contidos em todas as categorias 

### Requisitos
É necessário ter os seguintes requisitos instalados na máquina
1. Python 3.6
2. Biblioteca Scrapy - pip install Scrapy

### Modo de executação
1. Faça uma cópia do arquivo questao_1.py em sua máquina e salve-o em uma pasta de sua preferencia;
2. Abra o prompt de comando na pasta aonde está salvo o arquivo
3. Digite o seguinte comando e aparte enter - 'scrapy runsipder questao_1.py -o produtos.json'
4. O programa fará a extração das seguintes informações de todos os produtos
    - Descrição do Produto
    - Descrição do Fabricante
    - Url da Image do Produto

### Obs:
Não foi possível implementar o processo de realização de login nesse script, no entando o processo de raspagem foi implementado com sucesso!

## Questão 2
O presente script tem como objetivo realizar a pesquisa no site  https://pedidoeletronico.servimed.com.br de um pedido inputado como parâmetro pelo usuário e retornado com o valor e as informações dos campos Motivos e Itens(código, descrição, qtde faturada)

### Requisitos
É necessário ter os seguintes requisitos instalados na máquina
1. Python 3.6
2. Biblioteca Scrapy - pip install Scrapy

### Modo de executação
1. Faça uma cópia do arquivo questao_2.py em sua máquina e salve-o em uma pasta em uma pasta de sua preferencia
2. Abra o prompt de comando na pasta aonde está salvo o arquivo
3. Digite o seguinte comando e aparte enter - 'scrapy runsipder questao_2.py -o pedido.json'
4. O programa fará a extração das informações;

### Obs:
O código está incompleto estando funcionando apenas o processo de login. Os demais processos de busca pelo número do pedido e extração das informações não foram possíveis de serem implementadas

## Questão 3
O presente script tem como objetivo fazer o login no site http://coopertotal.nc7i.com/, criar um pedido e retornar o número do pedido criado junto com o status do mesmo em um arquivo .json 

### Requisitos
É necessário ter os seguintes requisitos instalados na máquina
1. Python 3.6
2. Biblioteca Requests - pip install requests

### Modo de executação
1. Faça uma cópia do arquivo questao_3.py em sua máquina e salve-o em uma pasta em uma pasta de sua preferencia
2. Abra o prompt de comando na pasta aonde está salvo o arquivo
3. Digite o seguinte comando e aparte enter - 'python3 questao_3.py'
4. O programa irá ser executado;

### Obs:
O código está incompleto estando funcionando apenas o processo de login. Os demais processos de inserção das informações, criação do pedido e extração das informações não foram possíveis de serem implementadas

## Questão 5
O presente script tem como objetivo criar uma árvore binária e realizar os seguintes testes de funcionalidade:

1. Pegar o valor de um nó
2. Verificar qual é o maior valor dos nós presente na árvore
3. Verificar se um determinado nó está presente na árvore

### Requisitos
É necessário ter os seguintes requisitos instalados na máquina
1. Python 3.6
2. Biblioteca unittest - pip install unittest

### Modo de executação
1. Faça uma cópia dos arquivos questao_5_teste_unit.py e questao_5_arvore.py em sua máquina e salve-os em uma pasta de sua preferencia;
2. Abra o prompt de comando na pasta aonde está salvo os arquivos
3. Digite o seguinte comando e aparte enter - 'python3 questao_5_teste_unit.py'
4. O pograma irá ser executado;

## Questão 6
O presente script tem como objetivo buscar todas as citações e informações (data/local de nascimento e descrição) sobre a autora "J.K. Rowling" presentes no site [quotes.toscrape.com](https://quotes.toscrape.com/)

### Requisitos
É necessário ter os seguintes requisitos instalados na máquina
1. Python 3.6
2. Biblioteca selenium - pip install selenium
3. Arquivo chromedriver.exe - baixado em https://chromedriver.chromium.org/downloads

### Modo de executação
1. Faça uma cópia do arquivo questao_6.py em sua máquina e salve-o em uma pasta de sua preferencia;
2. Abra o arquivo o arquivo e atualize o campo "DRIVE_PATH" com o endereço de onde está salvo o chromedrivre.exe
3. Salve e feche o arquivo .py
4. Abra o prompt de comando na pasta aonde está salvo o arquivo
5. Digite o seguinte comando e aparte enter - 'python3 questao_6.py'
6. O pograma irá ser executado;


## **Autor: Luiz Carlos Tavano Junior**

