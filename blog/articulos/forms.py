from django import forms
from .models import Comment
from .models import Entry

#Entrys
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
        
#Comentarios 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }