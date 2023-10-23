"""Models"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify

STATUS = ((0, "Draft"), (1, "Published"))
TERRIER_TYPE = [("Wired", "Wired"), ("Smooth", "Smooth")]
SEX_TYPE = [("Male", "Male"), ("Female", "Female")]
ADOPTION_TYPE = [("Adoption", "Adoption"), ("Rehome", "Rehome")]


class Adoption(models.Model):
    """
    Model for Adoption Page
    """
    terrier_type = models.CharField(
        max_length=10, choices=TERRIER_TYPE, null=False, blank=False)
    sex = models.CharField(
        max_length=10, choices=SEX_TYPE, null=False, blank=False)
    age = models.CharField(
        max_length=200, null=False, blank=False)
    why = models.CharField(
        max_length=200, null=False, blank=False)
    experience = models.CharField(
        max_length=200, null=False, blank=False)
    notes = models.CharField(
        max_length=200, null=False, blank=False)
    name = models.CharField(
        max_length=100, null=False, blank=False)
    email = models.EmailField(
        max_length=100, null=False, blank=False)
    adoption_type = models.CharField(
        max_length=10, choices=ADOPTION_TYPE, null=False, blank=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="adoption_author",
        default=1
    )
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)


class Post(models.Model):
    """
    Model for Post room specifically blog posts
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField('')
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """
    Model for the post room, specifically commenting
    """
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
