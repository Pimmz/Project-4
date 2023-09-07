from .models import Comment, Adoption, Rehome, Post 
from django import forms



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class AdoptionForm(forms.ModelForm):
    class Meta:
        model = Adoption
        fields = ('terrier_type', 'sex', 'age', 'why', 'experience', 'notes', 'name', 'email')

class RehomeForm(forms.ModelForm):
    class Meta:
        model = Rehome
        fields = ('terrier_type', 'sex', 'age', 'why', 'behaviour', 'notes', 'name', 'email')

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
