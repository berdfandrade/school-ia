# 📚 School Management System

A modern school management backend built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**. This system handles user registration, authentication, and role-based access for **students**, **teachers**, and **administrators**.

## 🚀 Features

- 🔒 Secure password hashing with `bcrypt`
- 🧠 Password validation policy (length, uppercase, number, special character)
- 👥 User roles: student, teacher, and admin
- 🧪 Isolated testing environment using `testcontainers` and PostgreSQL
- ⚙️ Clean service architecture for separation of responsibilities
- 📦 Environment-based configuration with `.env` support

## 📂 Tech Stack

- **FastAPI** – API framework
- **SQLAlchemy** – ORM for PostgreSQL
- **Pydantic** – Data validation and serialization
- **Testcontainers** – Integration testing with real PostgreSQL containers
- **Docker** – Optional for production or containerized environments

## 🧪 Testing

Testing uses `pytest` and `testcontainers` to ensure a clean database state for every test run. To run tests:

```bash
pytest
```

Ensure Docker is running locally since test containers require it.

## 🔧 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/school-api.git
   cd school-api
   ```

2. Set up your virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file based on `.env.example` and set your environment variables (e.g. database URL).

5. Run the API:
   ```bash
   uvicorn app.main:app --reload
   ```

## 📌 Project Structure

```
app/
├── models/          # SQLAlchemy models (User, Student, Teacher)
├── schemas/         # Pydantic schemas (UserCreate, etc.)
├── services/        # Business logic for users, students, teachers
├── config/          # Database setup and environment config
├── security/        # Password hashing and validation
├── tests/           # Unit and integration tests
└── main.py          # FastAPI app entry point
```
