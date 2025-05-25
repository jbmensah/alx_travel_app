# ALX Travel App

A Django-based REST API for travel listings and bookings, with Swagger documentation, MySQL backend, and Celery task queue.

---

## ✅ Status: Initial Setup Complete

- **Project scaffold**: `alx_travel_app` Django project & `listings` app created.
- **Dependencies installed & pinned** in `requirements.txt` (Django, DRF, CORS, django-environ, Celery, drf-yasg, mysqlclient, django-celery-results).
- **Environment variables** managed via `django-environ` (`.env` file).
- **MySQL** configuration applied in `settings.py`.
- **REST Framework** & **CORS** enabled.
- **Swagger UI** available at `/swagger/`.
- **Celery** stubbed out (RabbitMQ broker URL & results backend).
- **Git** initialized with an initial commit.

---

## 🛠 Getting Started (recap)

1. **Clone & activate venv**
   ```bash
   git clone https://github.com/your-org/alx_travel_app.git
   cd alx_travel_app
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure `.env`** (at project root):
   ```dotenv
   DJANGO_SECRET_KEY=...
   DEBUG=True
   DB_NAME=...
   DB_USER=...
   DB_PASSWORD=...
   DB_HOST=...
   DB_PORT=3306
   CELERY_BROKER_URL=amqp://guest:guest@localhost:5672//
   ```

4. **Run migrations & server**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. **Explore API docs**
   Open http://localhost:8000/swagger/ in your browser.

---

## 🚀 Next Steps

1. **Define the `Listing` model** in `listings/models.py` (e.g., `title`, `description`, `location`, `price`).
2. **Create a Serializer** (`listings/serializers.py`) for the Listing model.
3. **Implement a ViewSet** (`listings/views.py`) and register it with a DRF router in `listings/urls.py`.
4. **Write unit tests** for models, serializers, and API endpoints.
5. **Enhance Celery tasks** for background jobs (e.g., email notifications, data sync).
6. **Lock down CORS** and **set permissions** for production.

---


