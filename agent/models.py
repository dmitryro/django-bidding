from __future__ import unicode_literals

from django.db import models

# Agent Type model
class AgentType(models.Model):
    agent_type = models.CharField(max_length=100, blank=True, null=True)
    agent_code = models.CharField(max_length=100, blank=True, null=True)

# Auction model
class Agent(models.Model):
    reputation = models.FloatField(default=0,blank=True,null=True) 
    agent_type = models.ForeignKey(AgentType,blank=True,null=True)
    time_activated = models.DateTimeField(auto_now_add=True)
    time_passivated = models.DateTimeField(blank=True,null=True)
