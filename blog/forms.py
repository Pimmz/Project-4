from .models import Comment
from .models import Adoption
from .models import Rehome
from django import forms



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class AdoptionForm(forms.ModelForm):
    class Meta:
        model = Adoption
        fields = ('terrier_type', 'sex', 'age', 'why', 'experience', 'notes')

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