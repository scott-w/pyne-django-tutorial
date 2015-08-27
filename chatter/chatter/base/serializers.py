from rest_framework import serializers

from chatter.base.models import Chat


class ChatSerializer(serializers.ModelSerializer):
    """
    """
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Chat

    def create(self, validated_data):
        """
        """
        validated_data['user'] = self.context['view'].request.user
        return super(ChatSerializer, self).create(validated_data)
