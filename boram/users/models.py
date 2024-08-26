from django.db import models

# Create your models here.
# class Article(models.Model):
#     title = models.CharField(max_length=50)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     image = models.ImageField(upload_to="images/", blank=True)
#     author = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles")
#     like_users = models.ManyToManyField(
#         settings.AUTH_USER_MODEL, related_name="like_articles"
#     )