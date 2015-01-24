from django.views.generic import ListView

from chatter.base.models import Chat


class ChatListView(ListView):
    """List all chats in the system.
    """
    model = Chat
