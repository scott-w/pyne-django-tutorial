from django import forms

from chatter.base.models import Chat


class ChatForm(forms.ModelForm):
    """
    """
    class Meta:
        exclude = 'user', 'created'
        model = Chat
