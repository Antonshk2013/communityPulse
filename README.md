# 🧪 Flask JWT API

Простое Flask-приложение с авторизацией по JWT, использованием SQLAlchemy, Alembic для миграций и поддержкой переменных окружения.

---

## 🚀 Быстрый старт

### 🔧 1. Клонируй репозиторий и перейди в папку проекта

```bash
git clone https://github.com/your-username/flask-jwt-api.git
cd flask-jwt-api
```

### 📦 2. Установи зависимости

Рекомендуется использовать виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

### ⚙️ 3. Создай `.env` файл

Создай файл `.env` в корне проекта и укажи:

```
FLASK_ENV=development
FLASK_APP=app.py
DATABASE_URL=mysql+pymysql://user:password@localhost:3306/db_name
JWT_SECRET_KEY=your-secret-key
```

> ⚠️ Убедись, что база данных существует и доступна по указанному адресу.

### 🧱 4. Выполни миграции

```bash
flask db init        # только при первом запуске
flask db migrate -m "Initial migration"
flask db upgrade
```

### ▶️ 5. Запусти приложение

```bash
flask run
```

---

## 🔐 Эндпоинты

| Метод | Путь          | Описание                     | Защита     |
|-------|---------------|------------------------------|------------|
| POST  | `/register`   | Регистрация нового пользователя | ❌         |
| POST  | `/login`      | Авторизация и выдача JWT      | ❌         |
| GET   | `/protected`  | Пример защищённого ресурса     | ✅ JWT     |

---

## 📚 Зависимости

Указаны в `requirements.txt`:

```
alembic==1.16.2
annotated-types==0.7.0
blinker==1.9.0
click==8.2.1
Flask==3.1.1
Flask-Migrate==4.1.0
Flask-SQLAlchemy==3.1.1
greenlet==3.2.3
itsdangerous==2.2.0
Jinja2==3.1.6
Mako==1.3.10
MarkupSafe==3.0.2
pydantic==2.11.7
pydantic-settings==2.10.0
pydantic_core==2.33.2
PyMySQL==1.1.1
python-dotenv==1.1.0
SQLAlchemy==2.0.41
typing-inspection==0.4.1
typing_extensions==4.14.0
Werkzeug==3.1.3
```

---

## 🐳 Поддержка Docker (опционально)

Если хочешь, могу добавить `Dockerfile`, `docker-compose.yml` и инструкции.

---

## 📎 Примечания

- Используется MySQL через `PyMySQL`, но можно легко заменить на PostgreSQL или SQLite.
- Миграции выполняются с помощью Alembic через `Flask-Migrate`.
- Авторизация построена на `Flask-JWT-Extended`.

---

Если хочешь, я могу:
- добавить swagger-документацию (через `flasgger` или `apispec`);
- настроить логирование;
- добавить roles/permissions;
- сделать unit-тесты.

Хочешь что-то из этого?
