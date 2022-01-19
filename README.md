# ladyscomics

Crawler para extrair dados do blog http://ladyscomics.com.br/

Para rodar o spider que extrai os dados da página principal, postagens em geral, salvando os dados em um CSV: 
    scrapy crawl LadysComics -o file.csv -t csv 

Para rodar o spider que extrai os dados da página BAMQ!, que possui dados sobre as autoras do site, salvando os dados em um CSV: 
    scrapy crawl LadysBamq -o file.csv -t csv 
