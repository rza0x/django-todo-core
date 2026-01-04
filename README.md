# Django Todo Core

A dark-themed per-user Todo application built with Django.  
Each user can only see and manage their own todos.  
Auth (login / signup) is on the landing page. All views are class-based.

The project also exposes a REST API using Django REST Framework (DRF) and JWT authentication (SimpleJWT).

---

## Features

- User authentication (login & signup with password confirmation)
- Per-user Todo list (no access to other users' data)
- Full CRUD for todos (create, read, update, delete)
- Dark, glassmorphism-inspired UI
- Small vanilla JS for search/filter and subtle animations
- Class Based Views (CBV) for the HTML views
- REST API for todos (DRF)
- JWT authentication via `djangorestframework-simplejwt`
- Session authentication still works for browsable API

---

## Tech Stack

- Python / Django
- Django built-in auth
- Django REST Framework
- djangorestframework-simplejwt (JWT)
- python-dotenv (.env support for SECRET_KEY, etc.)
- Vanilla CSS & JS

---

## Setup

```bash
git clone https://github.com/rza0x/django-todo-core.git
cd django-todo-core

python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate

pip install django djangorestframework djangorestframework-simplejwt python-dotenv

python manage.py migrate
python manage.py createsuperuser  # optional
python manage.py runserver
