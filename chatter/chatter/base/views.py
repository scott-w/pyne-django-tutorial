from django.core.urlresolvers import reverse
from django.views.generic import CreateView, ListView

from chatter.base.forms import ChatForm
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


class ChatCreateView(CreateView):
    """Create a new Chat and attach it to the logged in user.
    """
    model = Chat
    form_class = ChatForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ChatCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('index')
