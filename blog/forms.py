from .models import Post
from django import forms


class AddPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'title',
            'description',
            'author',
            'image'
        ]

    def save(self):
        post = super(AddPostForm, self).save()
        return post
