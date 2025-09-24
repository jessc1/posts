Post API

frameworks:  django, django rest framework. database: postgres

## Endpoints:  http://127.0.0.1:8000/swagger/
* To get access to the api is necessary to register in  http://127.0.0.1:8000/api/auth/register/, with the username, email and password,
   copy the refresh token in the http://127.0.0.1:8000/api/auth/refresh/ to get the access token, then copy the access token in the others endpoints
* Login:  http://127.0.0.1:8000/api/auth/login/
* Users : list of users http://127.0.0.1:8000/api/users/
* Posts: http://localhost:8000/api/posts/ http methods: post, patch, delete
* Like post: http://localhost:8000/api/posts/id/like/
* Remove Like in post: http://localhost:8000/api/posts/id/remove_like/
* Like comment : localhost:8000/api/comment/8/like/
* Remove Like in comment: localhost:8000/api/comment/id/remove_like/
* Filter Post: http://localhost:8000/api/posts/?search=title
* Ordering Post: http://localhost:8000/api/posts/?ordering=author


commands:

 start the django server
```
 uv run --env-file .env python manage.py runserver
```

 to create database migration
```
 uv run --env-file .env python manage.py  makemigrations
```

applying  the migration
```
uv run --env-file .env python manage.py migrate
```
tests
```
uv run --env-file .env pytest
```