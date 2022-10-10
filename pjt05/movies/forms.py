from django import forms
from .models import Movie, Comment

class MovieForm(forms.ModelForm):
    genre_1 = '코미디'
    genre_2 = '공포/스릴러'
    genre_3 = '액션'
    genre_4 = '전쟁'
    genre_5 = 'SF'
    genre_6 = '느와르'
    genre_7 = '스포츠'
    genre_8 = '뮤지컬'
    genre_9 = '로맨스'
    genre_10 = '드라마'

    GENRE_CASE = [
        (genre_1, '코미디'),
        (genre_2, '공포/스릴러'),
        (genre_3, '액션'),
        (genre_4, '전쟁'),
        (genre_5, 'SF'),
        (genre_6, '느와르'),
        (genre_7, '스포츠'),
        (genre_8, '뮤지컬'),
        (genre_9, '로맨스'),
        (genre_10, '드라마'),
    ]

    title = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    audience = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    genre = forms.ChoiceField(
        choices=GENRE_CASE, 
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )

    score = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'step': '.1',
                'min': '0',
                'max': '10',
            }
        )
    )

    release_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'class': 'form-control',
            'type': 'date'
            }
        )
    )

    poster_url = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 8,
            }
        )
    )

    class Meta:
        model = Movie
        # fields = '__all__'
        exclude = ('user',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ('movie', 'user',)

    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        )
    )