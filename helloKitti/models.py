from django.db import models

# =================================================================== 
# CREATE TABLE Blogs (
#     id INTEGER PRIMARY KEY,
#     title VARCHAR(255),
#     author VARCHAR(255),
#     content TEXT,
#     imgPath VARCHAR(255),
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );
class Blogs(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content = models.TextField()
    imgPath = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

# =================================================================== 
# CREATE TABLE Users (
#     id INTEGER PRIMARY KEY,
#     name VARCHAR(32),
#     email VARCHAR(32),
#     avatar VARCHAR(255),
#     passsword VARCHAR(255)
# )
class Users(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    avatar = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id} {self.name}"


# =================================================================== 
# CREATE TABLE Comments (
#     id INTEGER PRIMARY KEY,
#     user INTEGER,  -- foreign key reference to Users table
#     post INTEGER,  -- foreign key reference to Blogs table
#     comment_text TEXT,
#     parent_comment_id INTEGER,  -- self-reference to Comments table
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );
class Comments(models.Model):
    user_id = models.ForeignKey(Users, related_name='comments', on_delete=models.CASCADE)
    post_id = models.ForeignKey(Blogs, related_name='comments', on_delete=models.CASCADE)
    comment_text = models.TextField()
    parent_comment_id = models.ForeignKey('self', related_name='replies', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

# =================================================================== 
# CREATE TABLE Likes (
#     id INTEGER PRIMARY KEY,
#     user INTEGER,  -- foreign key reference to Users table
#     post INTEGER,  -- foreign key reference to Blogs table
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );
class Likes(models.Model):
    user_id = models.ForeignKey(Users, related_name="likes", on_delete=models.CASCADE)
    post_id = models.ForeignKey(Blogs, related_name="likes", on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)

# =================================================================== 
# CREATE TABLE CommentLikes (
#     id INTEGER PRIMARY KEY,
#     comment INTEGER,  -- foreign key reference to Comments table
#     user INTEGER,  -- foreign key reference to Users table
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );
class CommentLikes(models.Model):
    comment_id = models.ForeignKey(Comments, related_name="comment_likes", on_delete=models.CASCADE)
    post_id = models.ForeignKey(Users, related_name="comment_likes", on_delete=models.CASCADE)
    likedat = models.DateTimeField(auto_now_add=True)

# =================================================================== 
# CREATE TABLE Testimonials (
#     id INTEGER PRIMARY KEY,
#     name VARCHAR(32),
#     designation VARCHAR(255),
#     comment TEXT,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );
class Testimonials(models.Model):
    name = models.CharField(max_length=32)
    designation = models.CharField(max_length=255, null=True)
    comment = models.TextField()
    said_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.designation})"