from rest_framework import serializers
from chatgpt.models import Conversation

class RandomUUIDSerializer(serializers.Serializer):
    data = serializers.UUIDField()
    
    
class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = [ 
                  'uuid',
                  'model', 
                  'title',
                  'data',
                  'datetime_field'
                  ]  # 或者指定要包含的特定字段列表  

