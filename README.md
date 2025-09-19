# 🛫 ALX Travel App

Django project with MySQL database, REST framework, CORS support, Celery, and Swagger API documentation.

---

## 🚀 Features

- Django + Django REST Framework
- MySQL database configuration with `.env`
- CORS support
- Swagger documentation at `/swagger/`
- Listings app with a sample endpoint

---

## 🛠 Installation

### 1. Clone Repo

```bash
git clone https://github.com/ufuos/alx_travel_app.git
cd alx_travel_app
```

📂 Project Structure
alx_travel_app/
├── alx_travel_app/
│ ├── **init**.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
├── listings/
│ ├── **init**.py
│ ├── admin.py
│ ├── apps.py
│ ├── migrations/
│ ├── models.py
│ ├── tests.py
│ ├── views.py
├── manage.py
├── requirements.txt
├── .env.example
├── README.md
<<<<<<< HEAD:README.md
"# alx_travel_app_0x00" 
=======

# alx_travel_app_0x00

## 🚀 Overview

This project extends **alx_travel_app** by adding:

- Database models (Listing, Booking, Review)
- API serializers
- Seeder management command

## 📂 Structure

- `listings/models.py` → Database models
- `listings/serializers.py` → API serializers
- `listings/management/commands/seed.py` → Seeder script

## ⚙️ Setup

```bash
git clone <your-repo-url>
cd alx_travel_app_0x00
pip install -r requirements.txt
python manage.py migrate
python manage.py seed
python manage.py runserver
```
>>>>>>> 00be49a3d467da74c7b6586952da899c91f8c93f:alx_travel_app/README.md
