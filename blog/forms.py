from .models import Comment
from .models import Adoption
from .models import Rehome
from django import forms



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class AdoptionForm(forms.Form):    
    fox_terrier_choice  = forms.TypedChoiceField(
        label="Which Fox terrier do you want to adopt?",
        choices=((1, "Wired"), (0, "Smooth")),
        widget=forms.RadioSelect,
        initial='1',
        coerce=int,
        required=True,
    )
    male_female = forms.TypedChoiceField(
        label="Would prefer a Male or Female?",
        choices=((1, "Male"), (0, "Female")),
        widget=forms.RadioSelect,
        initial='1',
        coerce=int,
        required=True,
    )
    What_age = forms.CharField(
        label="What age Fox Terrier, are you looking for?",
        required=False,
    )
    why_Fox = forms.CharField(
        label="Why would you like to adopt a Fox Terrier?",
        max_length=80,
        required=True,
    )
    dog_experience = forms.CharField(
        label="What experience with dogs do you have?",
        max_length=80,
        required=True,
    )

    notes = forms.CharField(
        label="Additional notes or feedback",
        required=False,
    )

class RehomeForm(forms.Form):
    fox_terrier_choice  = forms.TypedChoiceField(
        label="Which Fox terrier do you want to rehome?",
        choices=((1, "Wired"), (0, "Smooth")),
        widget=forms.RadioSelect,
        initial='1',
        coerce=int,
        required=True,
    )
    male_female = forms.TypedChoiceField(
        label="Is the Fox Terrier you wish to rehome Male or Female?",
        choices=((1, "Male"), (0, "Female")),
        widget=forms.RadioSelect,
        initial='1',
        coerce=int,
        required=True,
    )
    dog_age = forms.IntegerField(
        label="What age is the Fox Terrier you wish to rehome?",
        required=False,
    )

    rehome_reason = forms.CharField(
        label="Why do you want to rehome them?",
        max_length=80,
        required=True,
    )

    notes = forms.CharField(
        label="Additional notes or feedback",
        required=False,
    )   
    image_upload = forms.ImageField(
        label="Upload a picture of your Fox Terrier",
        required=False,
    )   