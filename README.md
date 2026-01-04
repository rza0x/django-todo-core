# Django Dark Todo

A minimalist dark-themed Todo application built with Django.  
Each user can only see and manage their own todos.  
Auth (login / signup) is on the landing page. All views are class-based.

## Features

- User authentication (login & signup with password confirmation)
- Per-user Todo list (no access to other users' data)
- Full CRUD for todos (create, read, update, delete)
- Dark UI inspired by glassmorphism
- Small JS for search/filter and subtle animations

## Tech Stack

- Python / Django
- Django built-in auth
- Class Based Views (CBV)
- Vanilla CSS & JS

## Setup

```bash
git clone https://github.com/rza0x/django-dark-todo.git
cd django-dark-todo

python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate

pip install django
python manage.py migrate
python manage.py createsuperuser  # optional
python manage.py runserver
