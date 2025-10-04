# 🎓 Student API - Django REST Framework

A simple backend project built using **Django REST Framework** for managing student data.  
This project is fully tested using **Postman**.

---

## 🚀 Features
- Create, Read, Update, and Delete student records (CRUD)
- Function-based API views
- JSON responses
- SQLite database (easy to replace with PostgreSQL/MySQL)

---

## ⚙️ Tech Stack
- Python 3.x
- Django 5.x
- Django REST Framework
- SQLite

---

## 🧠 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/<your-username>/student-api-django.git
cd student-api-django

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # on Windows
# or
source venv/bin/activate  # on macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
