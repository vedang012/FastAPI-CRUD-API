# FastAPI CRUD API

A simple RESTful CRUD API built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL** to learn Python backend development.

## Features

- Create a Product
- Get all Products
- Get Product by ID
- Update a Product
- Delete a Product
- PostgreSQL integration
- SQLAlchemy ORM
- Dependency Injection with FastAPI
- Automatic Swagger API documentation

---

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Uvicorn

---

## Project Structure

```
.
├── main.py
├── database.py
├── database_models.py
├── models.py
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Database

Update the PostgreSQL connection string in `database.py`.

```python
db_url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="",
    host="localhost",
    port=5432,
    database="fastapitest",
)
```

---

## Run the application

```bash
uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## API Documentation

Interactive Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

