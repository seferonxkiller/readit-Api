from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Article(models.Model):
    author = models.ForeignKey("profile.Profile", on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=221)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='articles/', null=True, blank=True)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey("profile.Profile", on_delete=models.SET_NULL, null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.author.user.get_full_name():
            return f"{self.author.user.get_full_name()}'s comment"
        return f"{self.author.user.username}'s comment"
