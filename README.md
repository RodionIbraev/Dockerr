Типовые команды для запуска контейнера c backend-сервером:
1) docker build . --tag=my_app
2) docker run -d -p 8000:8000 my_app

Примеры API-запросов: 

@baseUrl = http://localhost:8000/api

# получение датчиков
GET {{baseUrl}}/sensors/
Content-Type: application/json

###

# создание датчика
POST {{baseUrl}}/sensors/
Content-Type: application/json

{
  "name": "EQP32342",
  "description": "Датчик в ванной"
}

###

# обновление датчика
PATCH {{baseUrl}}/sensors/1/
Content-Type: application/json

{
  "description": "Перенес датчик в кабинет"
}

###

# добавление измерения
POST {{baseUrl}}/measurements/
Content-Type: application/json

{
  "sensor": 2,
  "temperature": 16.2
}

###

# получение информации по датчику
GET {{baseUrl}}/sensors/1/
Content-Type: application/json