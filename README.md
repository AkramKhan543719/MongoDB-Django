# Django + MongoDB Integration Exploration

A practical exploration of integrating **Django** with **MongoDB** using the official **PyMongo** driver.

This project demonstrates how a Django application can communicate with a MongoDB database, retrieve document-based data, and expose the data through a Django HTTP endpoint.

---

## 📌 Project Overview

This project was developed as an exploration of using Django with MongoDB.

The implementation demonstrates:

- Django project setup
- MongoDB local setup
- PyMongo integration
- MongoDB database connection
- MongoDB collection access
- Reading MongoDB documents through Django
- Django URL routing
- JSON responses
- NoSQL document-based data access

The project uses the same local MongoDB database created during the MongoDB exploration:

```
Database: college
Collection: students
```

---

## 🎯 Objectives

The objectives of this project are:

1. Explore Django framework fundamentals.
2. Understand Django's traditional relational database architecture.
3. Explore MongoDB as a NoSQL database.
4. Connect Django with MongoDB using PyMongo.
5. Retrieve MongoDB documents from a Django view.
6. Return MongoDB data as JSON.
7. Understand the difference between Django ORM and direct MongoDB access.
8. Compare Django's relational database workflow with MongoDB's document-based workflow.

---

## 🏗️ Architecture

```
                       CLIENT
                         │
                         │ HTTP Request
                         ▼
                 ┌────────────────┐
                 │     Django     │
                 │    Routing     │
                 └───────┬────────┘
                         │
                         ▼
                 ┌────────────────┐
                 │ Django View    │
                 │  students()    │
                 └───────┬────────┘
                         │
                         ▼
                 ┌────────────────┐
                 │    PyMongo     │
                 │ MongoDB Driver │
                 └───────┬────────┘
                         │
                         ▼
                 ┌────────────────┐
                 │    MongoDB     │
                 │ Local Server   │
                 └───────┬────────┘
                         │
                         ▼
                    ┌──────────┐
                    │ college  │
                    │ Database │
                    └────┬─────┘
                         │
                         ▼
                    ┌──────────┐
                    │ students │
                    │Collection│
                    └──────────┘
```

---

## 🧠 Django + MongoDB Concept

Django is traditionally designed around relational databases and its ORM.

Typical Django architecture:

```
Django
   ↓
Django ORM
   ↓
PostgreSQL / MySQL / SQLite
```

MongoDB uses a document-oriented model:

```
Django
   ↓
PyMongo
   ↓
MongoDB
```

Therefore, this project does not attempt to use Django's built-in relational ORM for MongoDB.

Instead, PyMongo is used directly to communicate with MongoDB.

---

## 🍃 MongoDB Data Model

MongoDB organizes data as:

```
MongoDB
   │
   └── Database
        │
        └── Collection
              │
              ├── Document
              ├── Document
              └── Document
```

Project database:

```
college
```

Collection:

```
students
```

Example document:

```json
{
  "_id": "ObjectId(...)",
  "name": "Akram",
  "age": 20,
  "department": "CSE",
  "specialization": "AIML"
}
```

---

## 🧩 Technology Stack

| Technology                     | Purpose                        |
|--------------------------------|--------------------------------|
| Python 3.9.9                   | Programming language           |
| Django 4.2.30                  | Web framework                  |
| PyMongo 4.18.1                 | MongoDB Python driver          |
| MongoDB 8.3.11                 | NoSQL database                 |
| Uvicorn / Django Dev Server    | Local development              |
| PowerShell                     | Development environment        |
| Git                            | Version control                |
| GitHub                         | Source code management         |

---

## 🔌 MongoDB Connection

The MongoDB connection is established using:

```python
from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017")

db = client["college"]

students_collection = db["students"]
```

Connection architecture:

```
Django
   │
   ▼
PyMongo MongoClient
   │
   ▼
mongodb://127.0.0.1:27017
   │
   ▼
college
   │
   ▼
students
```

---

## 📁 Project Structure

```
django-mongodb-explore/
│
├── django_mongodb/
│   ├── __init__.py
│   ├── asgi.py
│   ├── mongo.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── .gitignore
└── venv/                 # Local only, not committed
```

---

## 📄 MongoDB Connection Module

`mongo.py`:

```python
from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017")

db = client["college"]

students_collection = db["students"]
```

This module creates the MongoDB client and selects the required database and collection.

---

## 📄 Django View

`views.py`:

```python
from django.http import JsonResponse
from .mongo import students_collection


def students(request):
    data = []

    for student in students_collection.find():
        data.append({
            "id": str(student["_id"]),
            "name": student.get("name"),
            "age": student.get("age"),
            "department": student.get("department"),
            "specialization": student.get("specialization")
        })

    return JsonResponse(data, safe=False)
```

The view:

1. Connects to the MongoDB collection.
2. Retrieves documents.
3. Converts MongoDB ObjectId to a string.
4. Builds JSON-compatible data.
5. Returns the result through Django.

---

## 🌐 URL Routing

`urls.py`:

```python
from django.contrib import admin
from django.urls import path
from .views import students

urlpatterns = [
    path("admin/", admin.site.urls),
    path("students/", students),
]
```

The endpoint is:

```
GET /students/
```

---

## 📡 API Endpoint

### Get Students

```
GET /students/
```

URL:

```
http://127.0.0.1:8000/students/
```

Example response:

```json
[
  {
    "id": "6ab4ed062460da6814cd4b59",
    "name": "Akram",
    "age": 20,
    "department": "CSE",
    "specialization": "AIML"
  },
  {
    "id": "6ab4ed192460da6814cd4b5a",
    "name": "Rahul",
    "age": 20,
    "department": "CSE",
    "specialization": "AIML"
  },
  {
    "id": "6ab4eed5ab59a7f2b5f2e2c3",
    "name": "Vikram",
    "age": 22,
    "department": "CSE",
    "specialization": "AI"
  }
]
```

---

## 🔄 Request Flow

When the client requests:

```
GET /students/
```

the following process occurs:

```
1. Browser / Client
        │
        ▼
2. Django URL Router
        │
        ▼
3. students() View
        │
        ▼
4. PyMongo
        │
        ▼
5. MongoDB
        │
        ▼
6. college.students
        │
        ▼
7. MongoDB Documents
        │
        ▼
8. Django converts ObjectId → String
        │
        ▼
9. JsonResponse
        │
        ▼
10. Client
```

---

## 🆚 Django ORM vs PyMongo

| Feature                | Django ORM                     | PyMongo                       |
|------------------------|--------------------------------|-------------------------------|
| Primary database model | Relational                     | Document                      |
| Typical database       | PostgreSQL/MySQL/SQLite        | MongoDB                       |
| Data representation    | Models/Rows                    | Documents                     |
| Query style            | ORM methods                    | MongoDB queries               |
| Schema                 | Structured relational model    | Flexible document model       |
| MongoDB support        | Not native relational ORM      | Official MongoDB Python driver|
| MongoDB ObjectId       | Not native                     | Native                        |

---

## 🆚 Django + SQL vs Django + MongoDB

### Traditional Django

```
Django
   ↓
Django ORM
   ↓
PostgreSQL
   ↓
Tables
   ↓
Rows
```

### This Project

```
Django
   ↓
PyMongo
   ↓
MongoDB
   ↓
Collections
   ↓
Documents
```

---

## 🧪 Testing

The application was tested locally using the Django development server.

Start the server:

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/students/
```

The endpoint successfully retrieved documents from the MongoDB collection.

---

## ✅ Validation Results

The following components were successfully verified:

```
MongoDB Local Server             ✅
MongoDB Connection               ✅
MongoDB Database                 ✅
MongoDB Collection               ✅
PyMongo Installation             ✅
Django Installation              ✅
Django Project Setup             ✅
Django URL Routing               ✅
Django View                      ✅
PyMongo → MongoDB Communication  ✅
MongoDB Document Retrieval       ✅
ObjectId Conversion              ✅
JSON Response                    ✅
Django /students/ Endpoint       ✅
```

---

## 📊 Verified MongoDB Data

The final endpoint successfully returned:

```
Database: college
Collection: students
Documents: 3
```

Example records:

```
Akram
├── Age: 20
├── Department: CSE
└── Specialization: AIML

Rahul
├── Age: 20
├── Department: CSE
└── Specialization: AIML

Vikram
├── Age: 22
├── Department: CSE
└── Specialization: AI
```

---

## 🚀 Installation

### 1. Clone Repository

```bash
git clone https://github.com/AkramKhan543719/mongodb-django.git
cd mongodb-django
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

## 🗄️ Start MongoDB

Verify that the MongoDB service is running:

```powershell
Get-Service MongoDB
```

Expected:

```
Status   Name      DisplayName
Running  MongoDB   MongoDB Server (MongoDB)
```

---

## ▶️ Run Django

```bash
python manage.py runserver
```

The development server starts at:

```
http://127.0.0.1:8000/
```

Open the MongoDB endpoint:

```
http://127.0.0.1:8000/students/
```

---

## ⚠️ Django Migration Note

Django may display a message such as:

```
You have unapplied migration(s) for admin, auth,
contenttypes and sessions.
```

This project accesses MongoDB directly through PyMongo rather than using Django's built-in ORM for MongoDB.

The MongoDB demonstration endpoint does not depend on those relational migrations.

---

## 🔐 Security Considerations

This project is intended for local learning and exploration.

For production:

- Use MongoDB authentication.
- Store credentials in environment variables.
- Never hardcode passwords.
- Use secure connection strings.
- Enable TLS where appropriate.
- Validate and sanitize incoming data.
- Add authentication and authorization.
- Implement logging and monitoring.
- Use appropriate database permissions.

---

## 🔮 Future Improvements

The project can be extended with:

- MongoDB CRUD operations through Django
- Django REST Framework
- Authentication
- JWT authorization
- Student creation API
- Student update API
- Student deletion API
- Search and filtering
- Pagination
- MongoDB indexes
- Docker deployment
- Environment-based configuration
- Unit and integration testing
- Production database configuration

---

## 🎓 Learning Outcomes

This exploration provided practical understanding of:

- Django framework
- MongoDB
- NoSQL databases
- MongoDB collections
- MongoDB documents
- BSON/ObjectId
- PyMongo
- Django URL routing
- Django views
- JSON responses
- MongoDB integration patterns
- Django ORM limitations with document databases
- REST-style HTTP endpoints
- Git and GitHub

---

## 🧠 Key Technical Takeaway

Django's built-in ORM is primarily designed around relational databases.

For this exploration, MongoDB was accessed directly through the official PyMongo driver:

```
Django
   ↓
PyMongo
   ↓
MongoDB
```

This approach allows Django to use MongoDB's document-oriented data model without treating MongoDB as a relational database.

---

## 👨‍💻 Author

**Pathan Mohammed Akram Khan**

B.Tech — Computer Science & Engineering (AI/ML)

GitHub: [https://github.com/AkramKhan543719](https://github.com/AkramKhan543719)

---

## 📄 License

This project was developed for educational and internship learning purposes.