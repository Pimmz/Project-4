from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify

W = "Wired"
S = "Smooth"
M = "Male"
F = "Female"

STATUS = ((0, "Draft"), (1, "Published"))
TERRIER_TYPE = [(W, "Wired"), (S, "Smooth")]
SEX_TYPE = [(M, "Male"), (F, "Female")]

class Adoption(models.Model):
    terrier_type = models.CharField(max_length=10, choices=TERRIER_TYPE, verbose_name="Which Fox terrier do you want to adopt?", null=True, blank=True)
    sex = models.CharField(max_length=10, choices=SEX_TYPE, verbose_name="would prefer a Male or Female?", null=True, blank=True)
    age = models.CharField(max_length=200,verbose_name="What age Fox Terrier, are you looking for?", null=True, blank=True)
    why = models.CharField(max_length=200, verbose_name="Why would you like to adopt a Fox Terrier?", null=True, blank=True)
    experience = models.CharField(max_length=200, verbose_name="What experience with dogs do you have?", null=True, blank=True)
    notes = models.CharField(max_length=200, verbose_name="Additional notes or feedback", null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name="Your Name?", null=True, blank=True)
    email = models.EmailField(max_length=100, verbose_name="Your Email Address", null=True, blank=True)
    
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="adoption_author" ,default=1
    )
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)
        
W = "Wired"
S = "Smooth"
M = "Male"
F = "Female"

STATUS = ((0, "Draft"), (1, "Published"))
TERRIER_TYPE = [(W, "Wired"), (S, "Smooth")]
SEX_TYPE = [(M, "Male"), (F, "Female")]

class Rehome(models.Model):
    terrier_type = models.CharField(max_length=10, choices=TERRIER_TYPE, verbose_name="Which Fox terrier do you want to rehome?", null=True, blank=True)
    sex = models.CharField(max_length=10, choices=SEX_TYPE, verbose_name="Is your Fox Terrier Male or Female?", null=True, blank=True)
    age = models.CharField(max_length=200,verbose_name="What age is your Fox Terrier?", null=True, blank=True)
    why = models.CharField(max_length=200, verbose_name="Why would you like to rehome a Fox Terrier?", null=True, blank=True)
    behaviour = models.CharField(max_length=200, verbose_name="What are they like around other dogs?", null=True, blank=True)
    notes = models.CharField(max_length=200, verbose_name="Additional notes or feedback", null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name="Your Name?", null=True, blank=True)
    email = models.EmailField(max_length=100, verbose_name="Your Email Address", null=True, blank=True)
    
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="rehome_author",default=1
    )

    created_on = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return str(self.pk)
    
    
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
