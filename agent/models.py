from __future__ import unicode_literals

from django.db import models

# Agent Type model


class AgentType(models.Model):

    agent_type = models.CharField(max_length=100, blank=True, null=True)
    agent_code = models.CharField(max_length=100, blank=True, null=True)

    # Meta Class

    class Meta:
        verbose_name = 'agent type'
        verbose_name_plural = 'agent types'


# Auction model


class Agent(models.Model):

    reputation = models.FloatField(default=0, blank=True, null=True)
    agent_type = models.ForeignKey(AgentType, blank=True, null=True)
    time_activated = models.DateTimeField(auto_now_add=True)
    time_passivated = models.DateTimeField(blank=True, null=True)
    time_terminated = models.DateTimeField(blank=True, null=True)

    # Meta Class

    class Meta:
        verbose_name = 'agent'
        verbose_name_plural = 'agents'


# Agent Action Status


class ActionState(models.Model):

    state_status = models.CharField(max_length=100, blank=True, null=True)
    state_code = models.CharField(max_length=100, blank=True, null=True)

    # Meta Class

    class Meta:
        verbose_name = 'action state'
        verbose_name_plural = 'action states'


# Agent Action


class AgentAction(models.Model):
    action_goal = models.CharField(max_length=100, blank=True, null=True)
    action_state = models.ForeignKey(ActionState, blank=True, null=True)

    # Meta Class

    class Meta:
        verbose_name = 'agent action'
        verbose_name_plural = 'agent actions'
