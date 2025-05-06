* INSTRUCTIONS
* 1. Создание и активация виртуальной среды:
```bash
python -m venv venv
```
 - Активация:
 - - Linux:
```bash
. ./venv/bin/activate
```

 - - Windows:
```bash
venv\Scripts\activate
```

* 2. Установка зависимостей:
```bash
pip install -r requirements.txt
```

4. Запуск проекта:
```bash
docker compose up --build
```

6. Остановка проекта:
```bash
docker compose down
```

Для миграций:
```bash
flask db migrate -m "Migration description"
```

```bash
flask db upgrade
```

Для тестов создать БД:
```bash
createdb -U exam -h localhost exam_db_test
```