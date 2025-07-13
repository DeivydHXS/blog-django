# Blog Django

Projeto de blog desenvolvido com Django, Docker e PostgreSQL.

## Descrição

Este projeto é um blog simples, onde é possível criar categorias e postagens, utilizando Django como framework web e PostgreSQL como banco de dados, com ambiente pronto para desenvolvimento e produção via Docker.

## Tecnologias Utilizadas

- Python 3.13
- Django 4.2
- PostgreSQL 17
- Docker & Docker Compose

## Estrutura do Projeto

```
.
├── djangoapp/           # Código fonte do Django
│   ├── blog/            # Aplicação principal do blog
│   └── project/         # Configurações do projeto Django
├── data/                # Dados persistentes (media/static/postgres)
├── scripts/             # Scripts auxiliares (entrypoint Docker)
├── dotenv_files/        # Arquivos de ambiente (.env)
├── Dockerfile           # Dockerfile do projeto
├── docker-compose.yml   # Orquestração dos containers
└── README.md            # Este arquivo
```

## Como Executar

### 1. Clone o repositório

```sh
git clone https://github.com/deivydhxs/blog-django.git
cd blog-django
```

### 2. Configure as variáveis de ambiente

Copie o arquivo de exemplo e edite conforme necessário:

```sh
cp dotenv_files/.env-example dotenv_files/.env
```

Edite `dotenv_files/.env` e defina as variáveis, como `SECRET_KEY`, `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`.

### 3. Suba os containers com Docker Compose

```sh
docker-compose up --build
```

O Django estará disponível em [http://localhost:8000](http://localhost:8000).

### 4. Acesse o container para comandos administrativos

```sh
docker exec -it djangoapp sh
```

### 5. Criar superusuário (opcional)

Dentro do container:

```sh
python manage.py createsuperuser
```

## Comandos Úteis

- Rodar migrações manualmente:

```sh
python manage.py migrate
```

- Coletar arquivos estáticos:

```sh
python manage.py collectstatic
```

- Acessar o shell do Django:

```sh
python manage.py shell
```

- Rodar o servidor de desenvolvimento:

```sh
python manage.py runserver 0.0.0.0:8000
```

## Dicas

- Utilize o Docker Desktop para gerenciar os containers e volumes de forma mais fácil.
- Verifique os logs dos containers para depuração:

```sh
docker-compose logs -f
```

- Para parar os containers, utilize:

```sh
docker-compose down
```

## Referências

- [Documentação do Django](https://docs.djangoproject.com/)
- [Documentação do Docker](https://docs.docker.com/)
- [Canal Otavio Miranda](https://youtu.be/UNiRHn2iusg)