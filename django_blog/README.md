# Django Blog Project

This is a simple blog application built with Django.  
It allows users to register, log in, and create, update, and delete blog posts.  
Each post can have tags and user comments.

---

## Features
- User registration and authentication
- User profile update
- Create, read, update, and delete blog posts
- Add and manage comments
- Tag system for categorizing posts
- Search posts by title or content
- Intuitive URL structure

---

## Tech Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS (Django Templates)
- **Database:** SQLite (default)

---

## How to Run the Project Locally

1. **Clone this repository:**
   ```bash
   git clone <your_repo_url>
   cd django_blog

# Django Blog Project

This is a simple blog application built with Django.  
It allows users to register, log in, and create, update, and delete blog posts.  
Each post can have tags and user comments.

---

## Features
- User registration and authentication
- User profile update
- Create, read, update, and delete blog posts
- Add and manage comments
- Tag system for categorizing posts
- Search posts by title or content
- Intuitive URL structure

---

## Tech Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS (Django Templates)
- **Database:** SQLite (default)

---

## How to Run the Project Locally

1. **Clone this repository:**
   ```bash
   git clone <your_repo_url>
   cd django_blog

## 2. **Create and activate a virtual environment:**

python -m venv venv
venv\Scripts\activate      # (on Windows)
source venv/bin/activate   # (on Mac/Linux)


##  3. **Install dependencies:**

pip install -r requirements.txt


## 4. **Run migrations:**

python manage.py migrate


## 5. **Create a superuser:**

python manage.py createsuperuser


## 6. **Run the development server:**

python manage.py runserver


##  7. **Open your browser at:**

http://127.0.0.1:8000/

## URL Patterns
Functionality	URL Example
Homepage (list posts)	/
View a post	/post/1/
Create a post	/post/new/
Edit a post	/post/1/update/
Delete a post	/post/1/delete/
Add comment	/post/1/comments/new/
Edit comment	/comment/1/update/
Delete comment	/comment/1/delete/
Register	/register/
Profile	/profile/
Author

Pauline Ochere
Capstone Project — ALX Django Learn Lab