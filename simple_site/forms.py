from django import forms
from .models import Topic, Comments, UploadFile


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['topic']
        labels = {'topic': ''}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']
        labels = {'comment': 'New comment:'}
        widgets = {'comment': forms.Textarea(attrs={'cols': 42, 'rows': 5})}


class UploaFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ['upload_file']
