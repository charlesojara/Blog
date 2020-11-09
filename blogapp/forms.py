from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','slug','author','updated_on','content','created_on','status')

        widgets = {
            'title':forms.TextInput(attrs={'class':'skin'}),
            'slug':forms.TextInput(attrs={'class':'skin'}),
            'author':forms.Select(attrs={'class':'skin'}),
            'updated_on':forms.DateTimeField(attrs={'class':'skin'}),
            'content':forms.Textarea(attrs={'class':'skin'}),
            'created_on':forms.DateTimeField(attrs={'class':'skin'}),
            'status':forms.IntegerField(attrs={'class':'skin'}),
        }