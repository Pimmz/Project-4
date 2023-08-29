from .models import Comment
from .models import Adoption
from .models import Rehome
from django import forms



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class AdoptionForm(forms.Form):
    why_Fox = forms.CharField(
        label="Why would you like to adopt a Fox Terrier?",
        max_length=80,
        required=True,
    )
        
    like_website = forms.TypedChoiceField(
        label="Do you want to adopt a fox terrier?",
        choices=((1, "Yes"), (0, "No")),
        widget=forms.RadioSelect,
        initial='1',
        coerce=int,
        required=True,
    )

    dog_experience = forms.CharField(
        label="What experience with dogs do you have?",
        max_length=80,
        required=True,
    )

    favorite_number = forms.IntegerField(
        label="Favorite number",
        required=False,
    )

    notes = forms.CharField(
        label="Additional notes or feedback",
        required=False,
    )

class RehomeForm(forms.Form):
    why_Fox = forms.CharField(
        label="Why Fox Terrier?",
        max_length=80,
        required=True,
    )
        
    like_website = forms.TypedChoiceField(
        label="Do you want to adopt a fox terrier?",
        choices=((1, "Yes"), (0, "No")),
        widget=forms.RadioSelect,
        initial='1',
        coerce=int,
        required=True,
    )

    dog_experience = forms.CharField(
        label="What experience with dogs do you have?",
        max_length=80,
        required=True,
    )

    favorite_number = forms.IntegerField(
        label="Favorite number",
        required=False,
    )

    notes = forms.CharField(
        label="Additional notes or feedback",
        required=False,
    )   