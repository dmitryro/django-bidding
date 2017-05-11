from rest_framework import serializers
from models import AgentType


class AgentTypeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    agent_type = serializers.CharField(required=False,
                                       allow_blank=True,
                                       max_length=100)

    agent_code = serializers.CharField(required=False, allow_blank=True,
                                       max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `Agent` instance, given the validated data.
        """
        return AgentType.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Agent` instance, given the validated
data.
        """
        instance.agent_type = validated_data.get('agent_type',
                                                 instance.agent_type)
        instance.agent_code = validated_data.get('agent_codde',
                                                 instance.agent_code)
        instance.save()
        return instance
