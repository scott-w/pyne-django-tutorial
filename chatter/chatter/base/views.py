from django.views.generic import ListView

from chatter.base.models import Chat


class ChatListView(ListView):
    """List all chats in the system.
    """
    model = Chat


class UserChatListView(ListView):
    """List all chats filtered by username.
    """
    model = Chat
    template_name = 'base/chat_list.html'

    def get_queryset(self):
        """Use the view kwargs to get a list of Chats by user.
        """
        return self.model.objects.filter(
            user__username=self.kwargs['username'])
