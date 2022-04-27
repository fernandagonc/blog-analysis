# Extração de Dados de Blogs
> Crawler para extrair dados do site http://ladyscomics.com.br/ e https://minadehq.com.br/ 


Para a obtenção dos dados do site utilizou-se um framework open-source em Python, o Scrapy (https://docs.scrapy.org/en/latest), que permite web crawling e web scraping, de forma a extrair dados estruturados de páginas web.

## Lady's Comics

As principais seções de interesse do site são os Quadrinhos, os Especiais, as Entrevistas e os Eventos que possuem como conteúdo publicações das autoras e o BAMQ!, uma página em formato de tabela com os dados das autoras contribuintes do site. 

Foram desenvolvidos dois Spiders para extrair todos os dados de relevantes. Um com o objetivo de percorrer as publicações do site a partir da página inicial e outro para extrair dados do BAMQ! com os dados das autoras contribuintes do site, gerando, assim, dois arquivos CSVs a serem analisados. 

### Execução

Para rodar o spider que extrai os dados da página principal, postagens em geral, salvando os dados em um CSV: 
```
    scrapy crawl LadysComics -o file.csv -t csv 
```

Os resultados da consulta acima estão no csv *ladys.csv*


Para rodar o spider que extrai os dados da página BAMQ!, que possui dados sobre as autoras do site, salvando os dados em um CSV: 
```
    scrapy crawl LadysBamq -o file.csv -t csv 
```

Os resultados da consulta acima estão no csv *bamq.csv*

## Mina de HQ

## Visualizações dos dados
Diversas visualizações dos dados estão disponíveis em: https://docs.google.com/presentation/d/1Mr7s5mNtKR5qNLcxDf8ctbIOEoI9tYEAC6SY6_Lwy9g/edit?usp=sharing

