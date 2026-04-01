## Тестовое задание на позицию DevOps Effective Mobile

### Порядок запуска

1. скопировать `.env.example` в `.env`
2. запустить контейнеры `docker compose up -d`
3. проверить что контейнеры поднялись и работают `docker ps | grep effective-mobile`. в списке дожны быть 2 контенйра  

```
effective-mobile-nginx-1.0.0
effective-mobile-backend-1.0.0
```
где 1.0.0 это TAG указанный в файле .env

4. выполнить `curl http://localhost` убедиться что выдется сообщение в консоли `Hello from Effective Mobile!`

### Краткое описание архитектуры

Приложение состоит из двух контейнеров: `nginx` и `webserver`.

`nginx` принимает HTTP-запросы с хоста на порту `80` и работает как reverse proxy. Все входящие запросы он перенаправляет во внутренней Docker-сети `backend` на сервис `webserver`.

`webserver` запускает Python HTTP-сервер и слушает порт `8080` только внутри Docker-сети. Наружу этот порт не публикуется, поэтому доступ к backend возможен только через `nginx`.

### Используемые технологии

- Docker
- Docker Compose
- Nginx
- Python 3
- HTTP Server (`http.server`)

### Примечание
В проекте создан файл `requirements.txt` только для демонстрации загрузки зависимостей для облегченного образа

