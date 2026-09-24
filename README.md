\# 🐍 Django + MongoDB Exploration



A hands-on exploration of integrating \*\*Django\*\* with \*\*MongoDB\*\* using \*\*PyMongo\*\*, including a MongoDB-backed student endpoint.



\---



\## 📌 Overview



Django is traditionally built around a \*\*relational ORM\*\* (SQLite, PostgreSQL, MySQL). This project explores how to \*\*break away from that model\*\* and use Django with a \*\*NoSQL MongoDB\*\* backend — covering concepts, integration strategies, and a working MongoDB-backed endpoint.



It covers:



\- How Django normally handles databases (ORM, migrations, models)

\- MongoDB integration options with Django

\- Django models vs MongoDB documents

\- Connecting Django to MongoDB using \*\*PyMongo\*\*

\- Performing basic operations through a custom MongoDB-backed endpoint



\---



\## 🧰 Tech Stack



| Layer        | Technology          |

|--------------|----------------------|

| Framework    | Django               |

| Database     | MongoDB              |

| Driver       | PyMongo              |

| GUI Tool     | MongoDB Compass      |

| Language     | Python               |

| Server       | Django Dev Server    |



\---



\## 🧠 MongoDB Concepts Covered



\### 1. Document-Oriented Storage

Data is stored as \*\*BSON documents\*\* — flexible, JSON-like structures.



```json

{

&#x20; "\_id": ObjectId("..."),

&#x20; "name": "Akram Khan",

&#x20; "age": 22,

&#x20; "course": "Computer Science"

}

```



\### 2. Database → Collection → Document

| SQL (Django ORM) | MongoDB          |

|------------------|------------------|

| Database         | Database         |

| Table            | Collection       |

| Row              | Document         |

| Column           | Field            |

| Migration        | Not required     |



\### 3. Schema-less Design

Unlike Django models, MongoDB collections do \*\*not\*\* enforce schemas. This means \*\*no migrations\*\* are needed for MongoDB.



\### 4. `\_id` and ObjectId

Every document gets a unique `\_id`. This replaces Django's auto-incrementing `pk`.



\### 5. CRUD in MongoDB Shell

```js

db.students.insertOne({ name: "Akram", age: 22 })

db.students.find({})

db.students.updateOne({ name: "Akram" }, { $set: { age: 23 } })

db.students.deleteOne({ name: "Akram" })

```



\### 6. Indexing \& Aggregation

Same as SQL indexes \& GROUP BY, but more flexible:

```js

db.students.createIndex({ name: 1 })

db.students.aggregate(\[{ $group: { \_id: "$course", total: { $sum: 1 } } }])

```



\---



\## 🧠 Django Concepts Covered



\### 1. Traditional Django ORM Flow

```

Model → makemigrations → migrate → DB Table → QuerySet

```



\### 2. Why MongoDB Breaks This Flow

\- MongoDB is \*\*schema-less\*\* → no migrations

\- Django ORM expects relational tables

\- We bypass the ORM and use \*\*PyMongo\*\* directly



\### 3. Django Views

Views become the bridge between the HTTP request and the MongoDB collection.



\### 4. URL Routing

Standard Django `urls.py` routes requests to views.



\### 5. Settings

`settings.py` keeps `DATABASES` default (SQLite) for Django internals, but MongoDB handles the app's actual data.



\### 6. Integration Options

| Option                | Description                              |

|-----------------------|------------------------------------------|

| \*\*PyMongo (raw)\*\*     | Direct MongoDB driver — used here        |

| \*\*Djongo\*\*            | MongoDB as Django DB backend             |

| \*\*MongoEngine\*\*       | ODM (Object-Document Mapper) for Django  |



\---



\## 🔄 Flow Diagram



```

┌──────────────┐

│   Client     │  (Browser / Postman)

└──────┬───────┘

&#x20;      │ HTTP Request

&#x20;      ▼

┌──────────────────────────┐

│   Django URL Router      │

│   (django\_mongodb/urls)  │

└──────┬───────────────────┘

&#x20;      │

&#x20;      ▼

┌──────────────────────────┐

│   Django View            │

│   (views.py)             │

│   ┌──────────────────┐   │

│   │  No ORM used     │   │

│   │  PyMongo client  │   │

│   └────────┬─────────┘   │

└────────────┼─────────────┘

&#x20;            │ PyMongo Driver

&#x20;            ▼

┌──────────────────────────┐

│   MongoDB Server         │

│   ┌──────────────────┐   │

│   │  Database        │   │

│   │   └ Collection   │   │

│   │      └ Document  │   │

│   └──────────────────┘   │

└──────────┬───────────────┘

&#x20;          │

&#x20;          ▼

&#x20;   JSON Response

&#x20;          │

&#x20;          ▼

┌──────────────┐

│   Client     │

└──────────────┘

```



\---



\## 📁 Project Structure



```

django-mongodb-explore/

│

├── django\_mongodb/

│   ├── \_\_init\_\_.py

│   ├── asgi.py

│   ├── mongo.py          # MongoDB connection setup (PyMongo)

│   ├── settings.py

│   ├── urls.py

│   ├── views.py          # MongoDB-backed views

│   └── wsgi.py

├── manage.py

├── requirements.txt

├── .gitignore

└── README.md

```



\---



\## ⚙️ Setup Instructions



\### 1. Install MongoDB Locally

\- Download \*\*MongoDB Community Server\*\*

\- Install \*\*MongoDB Compass\*\*

\- Start the MongoDB service

\- Verify: `mongodb://localhost:27017`



\### 2. Clone the Repository

```bash

git clone https://github.com/AkramKhan543719/mongodb-django.git

cd django-mongodb-explore

```



\### 3. Create Virtual Environment

```bash

python -m venv venv

venv\\Scripts\\activate      # Windows

source venv/bin/activate   # macOS/Linux

```



\### 4. Install Dependencies

```bash

pip install -r requirements.txt

```



\### 5. Run the Django Server

```bash

python manage.py runserver

```



\- Server → `http://127.0.0.1:8000`



\---



\## 🔗 MongoDB Integration Notes



\- Django's default ORM is \*\*not used\*\* for MongoDB.

\- A dedicated `mongo.py` creates a \*\*PyMongo client\*\*.

\- Views interact with MongoDB collections \*\*directly\*\* (no migrations).

\- MongoDB stores data as flexible \*\*documents\*\* (BSON), unlike Django's rigid models.



\### Example MongoDB Document



```json

{

&#x20; "\_id": "ObjectId(...)",

&#x20; "name": "Akram Khan",

&#x20; "age": 22,

&#x20; "course": "Computer Science"

}

```



\---



\## 🧪 Testing



1\. Start MongoDB locally

2\. Run the Django server

3\. Access the MongoDB-backed endpoint via browser or Postman



\---



\## ✅ What I Learned



\- Django's traditional ORM vs MongoDB's document model

\- Why \*\*migrations don't apply\*\* to MongoDB

\- How to connect Django views to MongoDB using \*\*PyMongo\*\*

\- The trade-offs of using \*\*NoSQL\*\* with a Django backend

\- Structuring a Django project for \*\*non-relational\*\* data

\- When to use \*\*Djongo\*\* or \*\*MongoEngine\*\* vs raw PyMongo



\---



\## 👤 Author



\*\*Pathan Mohammed Akram Khan\*\*

🔗 GitHub: \[@AkramKhan543719](https://github.com/AkramKhan543719)

