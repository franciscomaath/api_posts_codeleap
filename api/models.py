from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    created_datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        ordering = ['-created_datetime']
    
    def __str__(self):
        return f'"{self.title}" by @{self.username}'
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_datetime']

    def __str__(self):
        return f'Comment by @{self.username} on post "{self.post.title}"'