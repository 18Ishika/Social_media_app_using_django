# Social_media_app_using_django


---

# 🐦 Django Tweet App

A simple **Twitter-inspired web app** built using **Django**, allowing users to register, log in, post tweets with optional images, and search through tweets by title or content. This project demonstrates key Django features such as models, views, templates, authentication, and database management.

---

## 🚀 Features

### 👤 User Authentication

* Register, log in, and log out functionality.
* Authenticated users can create tweets.
* Redirects unauthenticated users to the login page when they try to access restricted routes.

### 📝 Tweet Management

* Users can create and post tweets (with or without images).
* Each tweet includes a **title**, **text**, optional **photo**, and timestamps.
* Tweets are displayed in reverse chronological order (newest first).

### 🔍 Search Functionality

* Users can search tweets by **title** or **text** content.
* Search results are displayed dynamically on the same tweet listing page.

### 🖼️ Media Handling

* Uploaded images are saved inside the `/media/photos/` directory.
* Configurable media path via Django’s settings.

### 🧭 Navigation

* Navbar provides quick access to:

  * Home (Tweet List)
  * Create Tweet
  * Register / Login / Logout (based on authentication status)

### 🪄 Responsive UI

* Built with **Bootstrap 5** for clean, mobile-friendly design.
* Buttons styled with simple classes (`btn btn-primary`, `btn btn-outline-secondary`, etc.).
* Layout kept minimal and elegant for clarity.

---

## 🧩 Tech Stack

| Layer        | Technology Used                          |
| ------------ | ---------------------------------------- |
| **Backend**  | Django 5.x                               |
| **Frontend** | HTML5, CSS3, Bootstrap 5                 |
| **Database** | SQLite3 (default Django DB)              |
| **Language** | Python 3.10+                             |
| **Storage**  | Django Media Storage for uploaded images |

---

## 🗂️ Project Structure

```
Django/
│
├── tweetapp/                # Main app containing models, views, templates
│   ├── migrations/
│   ├── templates/
│   │   ├── tweet_list.html
│   │   ├── tweet_create.html
│   │   └── base.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
│
├── django_project/          # Root project folder
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── media/                   # Uploaded photos folder
├── manage.py
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/django-tweetapp.git
cd django-tweetapp
```

### 2️⃣ Create a virtual environment

```bash
python -m venv env
env\Scripts\activate   # On Windows
# OR
source env/bin/activate  # On macOS/Linux
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

*(If you don’t have a requirements.txt yet, you can generate it using `pip freeze > requirements.txt`)*

### 4️⃣ Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 6️⃣ Run the development server

```bash
python manage.py runserver
```

### 7️⃣ Open in browser

Visit 👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🧠 How It Works

1. When a new user registers, they’re redirected to the **Tweet List** page.
2. Logged-in users can create tweets with a title, text, and optional photo.
3. All tweets are displayed in descending order of creation time.
4. The search bar filters tweets dynamically by title or text.
5. Logout redirects the user back to the login page.

---







<img width="1358" height="644" alt="image" src="https://github.com/user-attachments/assets/080dc7aa-d0a8-4cde-abfd-8ab029a20ecc" />
