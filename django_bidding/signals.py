from django.dispatch import Signal

auction_new_requested = Signal(providing_args=["auction"])
auction_started = Signal(providing_args=["auction"])
auction_terminated = Signal(providing_args=["auction"])
auction_approved = Signal(providing_args=["auction"])
auction_over = Signal(providing_args=["auction"])
