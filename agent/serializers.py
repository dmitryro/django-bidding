from rest_framework import serializers
from models import AgentType
from models import ActionState
from models import AgentAction
from models import Agent


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
        Update and return an existing `AgentType` instance, given the validated
data.
        """
        instance.agent_type = validated_data.get('agent_type',
                                                 instance.agent_type)
        instance.agent_code = validated_data.get('agent_code',
                                                 instance.agent_code)
        instance.save()
        return instance


class ActionStateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    state_status = serializers.CharField(required=False,
                                         allow_blank=True,
                                         max_length=100)

    state_code = serializers.CharField(required=False, allow_blank=True,
                                       max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `ActionState` , given the validated data.
        """
        return ActionState.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `ActionState` instance
        """
        instance.state_status = validated_data.get('state_status',
                                                   instance.state_status)
        instance.state_code = validated_data.get('state_code',
                                                 instance.state_code)
        instance.save()
        return instance


class AgentActionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        """
        Create and return a new `AgentAction` , given the validated data.
        """
        return AgentAction.objects.create(**validated_data)


class AgentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        """
        Create and return a new `Agent` , given the validated data.
        """
        return Agent.objects.create(**validated_data)
