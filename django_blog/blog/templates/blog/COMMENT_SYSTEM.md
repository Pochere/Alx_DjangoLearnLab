# Comment System (blog app)

## Summary
Adds a Comment model and CRUD flows for comments on Posts.
Authenticated users can create comments. Only the comment author can edit or delete their comment.

## Model
`Comment` fields:
- post: ForeignKey -> Post (related_name='comments')
- author: ForeignKey -> settings.AUTH_USER_MODEL (related_name='comments')
- content: TextField
- created_at: DateTimeField(auto_now_add=True)
- updated_at: DateTimeField(auto_now=True)

## Forms
- `CommentForm` (ModelForm) with a single `content` field.

## Views
- `CommentCreateView` (LoginRequiredMixin, CreateView) — creates comment for a specific post (URL uses post_pk).
- `CommentUpdateView` (LoginRequiredMixin, UserPassesTestMixin, UpdateView) — author only.
- `CommentDeleteView` (LoginRequiredMixin, UserPassesTestMixin, DeleteView) — author only.

## URLs
- `post/<post_pk>/comments/new/` -> create comment
- `post/<post_pk>/comments/<pk>/edit/` -> edit comment
- `post/<post_pk>/comments/<pk>/delete/` -> delete comment

## Templates
- `post_detail.html` includes:
  - list of `object.comments.all`
  - inline comment form for authenticated users (`comment_form`)
- `comment_form.html` for edit/create pages
- `comment_confirm_delete.html` for delete confirmation

## How to use / test
1. Run migrations: `python manage.py makemigrations blog && python manage.py migrate`
2. Login or create a user.
3. Create a Post.
4. Open the post detail page and add a comment.
5. Edit/delete the comment as the author; verify other users cannot edit/delete it.

