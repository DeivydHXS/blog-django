# Anotações

Criar ambiente virtual python

```
python -m venv venv
```

```
venv/Scripts/Activate
```

```
python -m pip install --upgrade pip
```

```
pip install django
```

```
mkdir djangoapp
```

```
cd djangoapp
```

```
django-admin startproject project .
```

Para rodar comando django no docker
```
docker-compose run djangoapp python manage.py startapp blog
```

Para acessar o container diretamente
```
docker exec -it djangoapp sh
```