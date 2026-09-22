# Blog Application

A full-stack blog application built with **Django** and **Django REST Framework**.

## 🚀 Features

* User registration and login
* User logout
* User profile management
* Edit user profile
* Change password
* Forgot password
* Password reset
* Blog post management
* Profile image upload
* Blog post image upload
* Django REST Framework serializers
* SQLite database for development

## 🛠️ Technologies Used

* Python
* Django
* Django REST Framework
* HTML
* CSS
* JavaScript
* SQLite
* Git & GitHub

## 📂 Project Structure

```text
Blog-Application/
│
├── blog_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── blogapp/
│   ├── migrations/
│   ├── templates/
│   ├── forms.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── admin.py
│
├── media/
│   ├── posts/
│   └── profile/
│
├── requirements.txt
├── manage.py
├── .gitignore
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/jayson68/Blog-Application.git
```

### 2. Open the project folder

```bash
cd Blog-Application
```

### 3. Create a virtual environment

```bash
python -m venv .env
```

### 4. Activate the virtual environment

On macOS/Linux:

```bash
source .env/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run database migrations

```bash
python manage.py migrate
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open the application at:

```text
http://127.0.0.1:8000/
```

## 🔐 Authentication

The application includes:

* Registration
* Login
* Logout
* User profile
* Edit profile
* Change password
* Forgot password
* Password reset

## 🔌 REST API

The project uses **Django REST Framework** for API functionality.

Serializers are located in:

```text
blogapp/serializers.py
```

## 🗃️ Database

SQLite is used as the development database.

The local `db.sqlite3` file is excluded from Git using `.gitignore`.

## 📸 Media

Uploaded images are stored in:

```text
media/posts/
media/profile/
```

## 👨‍💻 Author

**Jayson Patrick**

GitHub: **jayson68**

## 📄 License

This project is created for learning and development purposes.
