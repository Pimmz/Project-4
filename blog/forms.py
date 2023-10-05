"""Forms"""
from .models import Comment, Adoption, Rehome, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class AdoptionForm(forms.ModelForm):
    class Meta:
        model = Adoption
        fields = ('name', 'email', 'terrier_type', 'sex', 'age', 'why',
                  'experience', 'notes')
        widgets = {
            'age': forms.Textarea(attrs={'cols': 100}),
            'why': forms.Textarea(attrs={'cols': 100}),
            'experience': forms.Textarea(attrs={'cols': 100}),
            'notes': forms.Textarea(attrs={'cols': 100}),
        }

    def clean(self):
        cleaned_data = super().clean()
        required_fields = ('terrier_type', 'sex', 'age', 'why',
                           'experience', 'notes', 'name', 'email')
        for field in required_fields:
            if not cleaned_data.get(field):
                self.add_error(field, "This field is required.")
        return cleaned_data


class RehomeForm(forms.ModelForm):
    class Meta:
        model = Rehome
        fields = ('terrier_type', 'sex', 'age', 'why',
                  'behaviour', 'notes', 'name', 'email')

    def clean(self):
        cleaned_data = super().clean()
        required_fields = ('terrier_type', 'sex', 'age', 'why',
                           'behaviour', 'notes', 'name', 'email')
        for field in required_fields:
            if not cleaned_data.get(field):
                self.add_error(field, "This field is required.")
        return cleaned_data


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'featured_image']
        widget = {
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'featured_image']
