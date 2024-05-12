from django import forms
from .models import Blog

class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea,required=True)
    
class ReplyForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea,required=True)
    

class AddBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = (
            "title",
            "slug",
            "category",
            "banner",
            "description"
        )