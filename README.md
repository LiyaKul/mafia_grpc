# Grpc Mafia

Реализация grpc-сервиса и клиента для него для игры в Мафию. Сервер запускается в докер контейнере с поддержкой запуска нескольких ботов, которые играют рандомно. По умолчанию в одной игре 4 игрока, 3 из которых - боты. Поменять количество можно в docker-compose файле в service:random_player:deploy:replicas. Запустить сервер можно из src командой:
```console
docker-compose build && docker-compose up
```
Обычный игрок запускается командой из src:
```console
pip3 install -r requirements.txt
python3 client.py
```
