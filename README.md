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

# ALX Travel App 0x00

![Django](https://img.shields.io/badge/Django-4.2-green)
![DRF](https://img.shields.io/badge/DRF-3.14-red)

## 📌 Project Overview

This project is a Django REST Framework-based travel app that allows users to browse listings, make bookings, and leave reviews.

## 🚀 Features

- Listings (CRUD)
- Bookings linked to users
- Reviews with ratings
- Database seeder for test data

## ⚙️ Setup

```bash
git clone https://github.com/<your-username>/alx_travel_app_0x00.git
cd alx_travel_app_0x00
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
