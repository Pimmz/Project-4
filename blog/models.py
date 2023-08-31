from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))
TERRIER_TYPE = [("W", "Wired"), ("S", "Smooth")]
SEX_TYPE = [("M", "Male"), ("F", "Female")]

class Adoption(models.Model):
    terrier_type = models.CharField(max_length=10, choices=TERRIER_TYPE, verbose_name="Which Fox terrier do you want to adopt?")
    sex = models.CharField(max_length=10, choices=SEX_TYPE, verbose_name="would prefer a Male or Female?")
    age = models.IntegerField(verbose_name="What age Fox Terrier, are you looking for?", default=0)
    why = models.CharField(max_length=200, verbose_name="Why would you like to adopt a Fox Terrier?")
    experience = models.CharField(max_length=200, verbose_name="What experience with dogs do you have?")
    notes = models.CharField(max_length=200, verbose_name="Additional notes or feedback")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="adoption_author"
    )
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username
        

class Rehome(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True)
    email = models.EmailField(max_length=100)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.title
    
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
