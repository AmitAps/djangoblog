from django import forms
from .models import Comment

#Rememberthat Django has two base classes to build forms: Form and ModelForm .
class EmailPostForm(forms.Form):
    """
    base class: form
    """
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


#For a list of all form fields available, you can visit https://docs.djangoproject.com/en/3.0/ref/forms/fields/ .

class CommentForm(forms.ModelForm):
    """
    base class: ModelForm
    To create a form from a model, you just need to indicate which model to use to build
    the form in the Meta class of the form. Django introspects the model and builds the form dynamically for you.
    Read more about 'Meta'.
    """
    class Meta:
        model = Comment
        fields = ('name','email','body')
