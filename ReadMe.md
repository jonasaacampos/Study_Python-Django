<p align="center">
<a href='https://github.com/jonasaacampos'><img src='https://img.shields.io/badge/feito%20com%20%E2%9D%A4%20por-jaac-cyan'></a>
<a href='https://www.linkedin.com/in/jonasaacampos'><img src='https://img.shields.io/badge/LinkedIn-Profile-informational?style=flat&logo=linkedin&logoColor=white&color=0D76A8'></a>
</p>

<p align="center">
   <a href='https://github.com/jonasaacampos'>
      <img alt="" src="https://img.shields.io/static/v1?color=blue&label=django&message=framework&style=for-the-badge&logo=django"/>
      </a>
      <img alt="" src="https://img.shields.io/static/v1?color=green&label=python&message=programing&style=for-the-badge&logo=python"/>
      </a>
</p>

<h1>Desenvolvimento Web com Django Framework</h1>

<img alt="logo desc..." src="img/django-hexbin.png" width=150 align=right>


> Python ? uma linguagem promissora para diversos fins com destaque para
> - IA
> - Computa??o Qu?ntica
> 
> O Django ? um framework poderoso e completo que utiliza python para aplica??es web.
>
> Aqui temos anota??es gerais para futuras consultas. ? meu primeiro contato com este framewor, e h? um [Projeto aqui](DjangoProjects) para consulta.

<h2>?ndice</h2>

- [Base de programa??o web](#base-de-programa??o-web)
- [Django B?sico](#django-b?sico)
  - [Instala??o](#instala??o)
  - [Criar projeto](#criar-projeto)
  - [Rodar Projeto](#rodar-projeto)
  - [MTV Deseign Pattern](#mtv-deseign-pattern)
  - [Migrations](#migrations)
  - [Area admin](#area-admin)
  - [Models](#models)
  - [Django shell](#django-shell)
- [Refer?ncias](#refer?ncias)


<!-- 
<details>
<summary>

## Base de programa??o web
</summary>

</details> 
-->

<details>
<summary>

## Base de programa??o web
</summary>
> Anota??es gerais sobre programa??o web


**Protocolos http e seus verbos**

- ? um dos protocolos mais importantes e utilizados no mundo.
- a porta padr?o sem critografia ? a 80 (http)
- a por com criptografia ? a 443 (https)
- [documenta??o oficial](1]https://tools.ietf.org/html/rfc7540)

![Principais verbos http](img/01_http-verbs.png)

**Linguagens Est?ticas X Din?micas**

- Linguagens est?ticas: n?o s?o processadas no servidor, renderizada no navegador.
- Linguagens din?micas: s?o processadas no servidor

![Frontend e Backend](img/02_frontend_backend.png)

**HTML, CSS e JS**

- HTML ? um arquivo de texto com marca??es (texto com vitaminas). Somente com o html j? temos uma p?gina web. Mas ? um site pelado.
- CSS ? a est?tica de um arquivo html. Veste o html ? rigor, deixando a p?gina apresent?vel. Com o css podemos tramalhar com:
  - `elemento`
  - `.` classe
  - `#` id
- JavaScript (nome de batismo => Ecma Script) completa a tr?ade do frontend. Serve para interatividade com o usu?rio
  - usar os scripts js no final do arquivo, evita inconvenientes, pois teremos todos os elementos j? carregados antes de quaisquer intera??es.

![Alt text](img/03_js.png)

**Frameworks Frontend**

- [Bootsrap](https://getbootstrap.com.br)
- Bulma

</details>


<details>
<summary>

## Django B?sico
</summary>

### Instala??o

- Usar `virtual env`
- `pip install django`
- `pip freeze > requiriments.txt`
- rodar virtual env `.venv/Scripts/Activate.ps1`
- 
### Criar projeto

- `django-admin startproject nomeProjeto .` O "." ao final da instru??o ? para que o projeto seja criado no diret?rio atual, e n?o em um subdiret?rio
- `django-admin startapp NomeDoApp`
- inserir o nome do app criado dentro do `settings.py` do projeto, na lista de `INSTALLED_APPS `.
- adicionar o diret?rio de templates dentro da vari?vel `TEMPLATES` no settings.py

### Rodar Projeto

- `python manage.py runserver`

### MTV Deseign Pattern

![Alt text](img/04_django-mtv-logo.png)

- quem tem as views s?o as aplica??es, e n?o o projeto
- as views s?o fun??es python
  ```
  def index(request):
    return render(request, "index.html")

  def contato(request):
    return render(request, "contato.html")
  ```
- por padr?o as `urls` s?o do projeto, e n?o na aplica??o.

![MTV](img/04_django-mtv.png)

### Migrations

- `python .\manage.py makemigrations`
- `python .\manage.py migrate`

### Area admin

- `python .\manage.py createsuperuser`

### Models

? um modelo de dados


```python
# retorna no console todos os dados da requisi??o
dict_request_data = request.headers
  for k, v in dict_request_data.items():
    print(f"{k}: {v}")
```

### Django shell

dir(nomeObjeto) -> mostra todos os m?todos que podemos usar no objeto


Inserir arquivos est?ticos
- `{% load static %}` no cabe?alho do html
- `<link rel="stylesheet" href="{% static 'css/bulma.css' %}">` como refer?ncia

**No arquivo `settings.py`**

```python
# usado durante o desenvolvimento
STATIC_URL = "static/"
# usado para produ??o
STATIC_ROOT = Path(BASE_DIR, "static_files")
```

</details> 

## Refer?ncias

- [Django Docs](https://docs.djangoproject.com/en/4.1/)