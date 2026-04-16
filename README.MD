# FastAPI API Key & Rate Limiting Service

## 📌 Overview

This project is a backend service built using FastAPI that provides API key-based authentication and enforces rate limiting on protected endpoints.

---

## 🚀 Features

* Generate unique API keys
* Track API usage per key
* Enforce rate limiting (5 requests per minute)
* Protected API endpoint
* Swagger documentation available at `/docs`

---

## 🛠️ Tech Stack

* FastAPI
* SQLite
* SQLAlchemy
* Pydantic

---

## ▶️ Setup Instructions

1. Clone the repository:

git clone https://github.com/akshithatirnathi05/fastapi-api-key-rate-limiter.git
cd fastapi-api-key-rate-limiter

2. Create virtual environment:

python -m venv .venv
.\.venv\Scripts\activate

3. Install dependencies:

pip install -r requirements.txt

4. Run the server:

uvicorn app.main:app --reload

---

## 🔑 API Endpoints

### 1. Generate API Key

* POST `/generate-key`
* Returns a unique API key

---

### 2. Access Protected API

* GET `/protected`
* Requires header:

x-api-key: YOUR_API_KEY

---

## ⚙️ Rate Limiting

* Limit: 5 requests per minute per API key
* If exceeded → returns `429 Too Many Requests`

---

## 🧪 Testing

You can test the APIs using:

- Swagger UI → http://127.0.0.1:8000/docs  
- Postman (import the provided collection)

---

## 📬 API Documentation

Swagger UI:

http://127.0.0.1:8000/docs

---

## 📄 Postman Collection

The file `postman_collection.json` is included in the repository.

Import it into Postman to test all endpoints easily.

---

## ⚠️ Assumptions

* Fixed time window rate limiting is used
* SQLite database is used for simplicity
* Single-instance backend system

---

## 📌 Notes

* Each API key is uniquely generated using UUID
* Request count and timestamps are stored in the database
* Rate limiting is enforced per API key