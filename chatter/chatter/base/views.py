from rest_framework import viewsets

from chatter.base.models import Chat
from chatter.base.serializers import ChatSerializer


class ChatViewSet(viewsets.ModelViewSet):
    """Manage Chats.
    """
    model = Chat
    serializer_class = ChatSerializer
    queryset = Chat.objects.select_related('user')
    search_fields = 'user__username', 'content'
