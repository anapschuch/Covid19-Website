# Projeto CES-22 - 2º bimestre
Projeto de CES - 22 do 2º bimestre

Integrantes:

  Ana Paula Schuch

  Artur Assis Alves

  Vinícius Brito Bastos Antunes
  
  
###### Link: https://base-epidemiologica.herokuapp.com/


### OBS: 
1 - Os pacotes que precisam ser instalados na máquina do desenvolvedor se encontram no arquivo requirements-dev.txt. O arquivo requirements.txt será utilizado para fazer deploy no servidor e ele chamará o arquivo requirements-dev.txt para instalar todos pacotes dele além de instalar mais dois, que não precisam ser instalados na máquina do desenvolvedor.

2 - É importante não publicar as variáveis SECRET_KEY e DEBUG. Por isso, utilizar a lib decouple pode ajudar.

3 - É necessário incluir EMAIL_HOST_USER e EMAIL_HOST_PASSWORD nas variáveis de ambiente. Elas se referem ao e-mail que envia mensagem de recuperação de senha.


#### Para rodar localmente:

Instalar os pacotes descritos abaixo. 

Configurar as variáveis SECRET_KEY, DEBUG, EMAIL_HOST_USER e EMAIL_HOST_PASSWORD. Para rodar localmente SECRET_KEY pode ser uma cadeia de caracteres quaisquer, DEBUG = True e para o e-mail basta configurar com um e-mail seu.

Rodar no terminal:

``` 
python3 manage.py makemigrations
python3 manage.py migrate
```

Após isso, basta iniciar o servidor:
 
 ```
python3 manage.py runserver
```


### Instalar os seguintes pacotes para iniciar o servidor:

  python               3.7.7

  django               3.0.8

  matplotlib           3.3.0   

  pandas               1.1.0          

  django-widget-tweaks 1.4.8

  mpld3

  reportlab            3.5.46  


#### Para realizar o deploy no Heroku, foi utilizado o tutorial: https://github.com/Gpzim98/django-heroku

#### Tutoriais utilizados para construção do site:

https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/

https://tutorial.djangogirls.org/pt/

https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p
