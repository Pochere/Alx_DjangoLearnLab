# Social Media API

This project is part of the **ALX Django Learn Lab** program.  
It is a Django REST Framework-based social media API that allows users to:

- Register and authenticate using a custom user model
- Create, view, update, and delete posts
- Comment on posts and view comments
- Filter and search through posts
- Manage user profiles with bio, profile pictures, and follower relationships
- Follow/unfollow other users and view a feed from followed users

---

## Technologies Used

- Python 3
- Django
- Django REST Framework
- SQLite (for development)

---

## Project Structure

social_media_api/
│
├── accounts/ # Handles user registration, login, and profiles
├── posts/ # Handles posts and comments
├── social_media_api/ # Project configuration files
└── venv/ # Virtual environment (ignored by Git)

## Running the Project Locally

1. **Activate your virtual environment:**

venv\Scripts\activate # Windows

OR on macOS/Linux:
source venv/bin/activate

2. **Install dependencies (if not done yet):**

pip install -r requirements.txt



3. **Run migrations:**

python manage.py makemigrations
python manage.py migrate



4. **Start the development server:**

python manage.py runserver


5. **Open your browser and navigate to the API endpoints:**

http://127.0.0.1:8000/api/posts/
http://127.0.0.1:8000/api/accounts/register/
http://127.0.0.1:8000/api/accounts/login/
http://127.0.0.1:8000/api/posts/feed/


---

## API Endpoints Overview

### Accounts

| Endpoint | Method | Description |
|----------|--------|-------------|
| /api/accounts/register/ | POST | Register a new user |
| /api/accounts/login/ | POST | Login and get authentication token |
| /api/accounts/profile/ | GET | Get or update user profile (authenticated only) |
| /api/accounts/follow/<user_id>/ | POST | Follow a user (authenticated only) |
| /api/accounts/unfollow/<user_id>/ | POST | Unfollow a user (authenticated only) |

### Posts

| Endpoint | Method | Description |
|----------|--------|-------------|
| /api/posts/ | GET, POST | List all posts or create a new post |
| /api/comments/ | GET, POST | List all comments or create a comment |
| /api/posts/feed/ | GET | Get posts from users you follow (authenticated only) |

---

## Notes

- Only authenticated users can create posts, comments, follow/unfollow users, and view their feed.
- The `following` relationship is managed through the custom `CustomUser` model.
- Feed endpoint aggregates posts from all users that the current user follows.
- Search functionality is enabled on `title` and `content` fields for posts.


## Testing

You can use **Postman** or **curl** to test API endpoints.  
Include authentication tokens in the header for protected routes:
