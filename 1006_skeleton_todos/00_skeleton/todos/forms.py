from django import forms
from .models import Todo, Comment


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        # fields = '__all__'
        exclude = {'user'}

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ('todo',)