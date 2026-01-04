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

You can run the project either **locally (without Docker)** or using **Docker / Docker Compose**.

### Option 1 – Local development (no Docker)

Clone the repo and create a virtualenv:

    git clone https://github.com/rza0x/django-todo-core.git
    cd django-todo-core

    python -m venv venv
    # Linux / macOS:
    # source venv/bin/activate
    # Windows (PowerShell):
    # venv\Scripts\Activate.ps1

Install dependencies:

    pip install django djangorestframework djangorestframework-simplejwt python-dotenv

Make sure you have a `.env` file with at least:

    SECRET_KEY=your-django-secret-key
    DEBUG=True

Run migrations and start the dev server:

    python manage.py migrate
    python manage.py createsuperuser  # optional
    python manage.py runserver

The app will be available at:

    http://localhost:8000

---

### Option 2 – Using Docker / Docker Compose

#### Requirements

- Docker (Docker Desktop on Windows/macOS)
- Docker Compose (included in recent Docker Desktop versions)

#### Steps

Clone the repo:

    git clone https://github.com/rza0x/django-todo-core.git
    cd django-todo-core

Create your `.env` file (SECRET_KEY, etc.):

    SECRET_KEY=your-django-secret-key
    DEBUG=True

Build and run containers:

    docker compose up --build

The Django dev server will run inside a container and be exposed on:

    http://localhost:8000

To stop the containers:

    docker compose down

---

## Docker files (overview)

- `Dockerfile` – builds a Python 3.12 image for the Django app
- `docker-compose.yml` – runs the app service with:
  - port `8000:8000`
  - `.env` file loaded into the container
  - project directory mounted into `/app` for easy local development

---

## Environment variables

The project expects a `.env` file in the project root. A simple example:

    SECRET_KEY=your-django-secret-key
    DEBUG=True

(Do **not** commit your real `.env` to Git.)

---

## License

[MIT](LICENSE)
