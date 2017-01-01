from __future__ import unicode_literals

from django.db import models

# Auction Type model
class AuctionType(models.Model):
    auction_type = models.CharField(max_length=100,blank=True,null=True)
    auction_code = models.CharField(max_length=100,blank=True,null=True)

# Auction model
class Auction(models.Model):
    reservation_price = models.FloatField(default=0,blank=True,null=True) 
    auction_type = models.ForeignKey(AuctionType,blank=True,null=True)
    time_started = models.DateTimeField(auto_now_add=True)
    time_ended = models.DateTimeField('Time Ended',blank=True,null=True)
