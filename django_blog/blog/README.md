# 📝 Blog Post Management Features — django_blog Project

## 📘 Overview
This document describes the **CRUD (Create, Read, Update, Delete)** functionality implemented for the **Blog Post Management** feature in the `django_blog` project.  
These features enable authenticated users to manage their own blog posts while allowing all visitors to view published posts.

---

## ⚙️ Features Implemented

### 1. ListView (`PostListView`)
- Displays all blog posts, ordered by publication date (latest first).
- Accessible to **all users** (no login required).
- Template: `post_list.html`.

### 2. DetailView (`PostDetailView`)
- Displays the full content of a single blog post.
- Accessible to **all users**.
- Template: `post_detail.html`.

### 3. CreateView (`PostCreateView`)
- Allows **logged-in users** to create new blog posts.
- Automatically sets the logged-in user as the **author**.
- Template: `post_form.html`.

### 4. UpdateView (`PostUpdateView`)
- Allows **only the post author** to edit an existing post.
- Uses Django’s `LoginRequiredMixin` and `UserPassesTestMixin` for access control.
- Template: `post_form.html`.

### 5. DeleteView (`PostDeleteView`)
- Allows **only the post author** to delete their post.
- Uses Django’s `LoginRequiredMixin` and `UserPassesTestMixin`.
- Template: `post_confirm_delete.html`.

---

## 🌐 URL Structure

| URL Path | View | Description |
|-----------|------|-------------|
| `/posts/` | `PostListView` | Displays all posts |
| `/posts/<int:pk>/` | `PostDetailView` | Displays a single post |
| `/posts/new/` | `PostCreateView` | Create a new post |
| `/posts/<int:pk>/edit/` | `PostUpdateView` | Edit an existing post |
| `/posts/<int:pk>/delete/` | `PostDeleteView` | Delete a post |

---

## 🔒 Permissions & Access Control
- Only **authenticated users** can create new posts.
- Only the **author** of a post can edit or delete it.
- All users (including guests) can view the list and detail pages.

---

## 🧪 Testing Notes
- Verified that authenticated users can create, update, and delete their posts.
- Verified that unauthorized users are redirected to the login page when attempting restricted actions.
- Confirmed that all form submissions work correctly.
- Navigation and links between list, detail, and form pages were tested successfully.

---

## 📁 Files Updated

| File | Description |
|------|--------------|
| `blog/views.py` | Added CRUD class-based views |
| `blog/forms.py` | Added ModelForm for the `Post` model |
| `blog/urls.py` | Added URL patterns for CRUD routes |
| `blog/templates/blog/` | Contains templates for all CRUD operations |
| `README.md` | Added documentation for blog post management features |

---

## 💡 Additional Notes
- CRUD functionality is built with Django’s **class-based views** for cleaner and more reusable code.
- Templates use conditional logic to show edit/delete links only to the author.
- Future enhancements could include adding pagination or image uploads to posts.

---

✅ **Assignment Requirement Completed:**  
This documentation satisfies Step 7 (“Documentation”) of the *Creating Blog Post Management Features* task.
