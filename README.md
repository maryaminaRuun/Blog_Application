# 📝 Blog Application

This is a Django-based blog application that supports user management, blog posts, and custom templates. It includes multiple apps: `blog` and `members`, with database and static/template support.

---

## 📁 Project Structure

BLOG_APPLICATION/
│
├── env/ # Virtual environment (excluded from version control)
├── mysite/ # Project root
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── blog/ # Blog app
│ ├── migrations/
│ ├── static/
│ ├── templates/
│ ├── templatetags/
│ ├── admin.py
│ ├── apps.py
│ ├── feeds.py
│ ├── forms.py
│ ├── models.py
│ ├── sitemaps.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
│
├── members/ # Members/user authentication app
│ ├── migrations/
│ ├── templates/
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
│
├── db.sqlite3 # SQLite database file
├── manage.py # Django management script
└── mysite_data.json # Optional project data dump


---

## 🚀 Features

- ✅ User registration and login (`members` app)
- ✅ Post creation, update, and delete (`blog` app)
- ✅ Feed and sitemap support
- ✅ Custom template tags and static file structure
- ✅ Django admin integration
- ✅ SQLite database for development
- ✅ Clean modular design with two separate apps

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Blog_Application.git
cd Blog_Application

2. Set Up Virtual Environment
bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
3. Install Dependencies
bash
pip install django

4. Run Migrations
bash
python manage.py makemigrations
python manage.py migrate

5. Run the Development Server
bash
python manage.py runserver
Then visit: http://127.0.0.1:8000

👩‍💻 Admin Access
To create a superuser:

bash
Copy
Edit
python manage.py createsuperuser
🧪 Running Tests
bash
Copy
Edit
python manage.py test

📦 Deployment
This app is ready for deployment on platforms like Heroku, PythonAnywhere, or Render. Be sure to:

Switch to PostgreSQL for production.

Set DEBUG = False in settings.py.

Use environment variables for sensitive data.

Set up static files handling with collectstatic.

📄 License
This project is licensed under the MIT License.

🙋‍♀️ Author
Maryama Ruun
Contact: [maryamiinaruun6@gmail.com]
GitHub: https://github.com/maryaminaRuun
---

Let me know if you'd like a version of this with badges (GitHub, Django, Python) or help with writing a `requirements.txt` or `.gitignore`.








