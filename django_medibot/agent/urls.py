from django.conf.urls import url
from admin_tools.menu import views

urlpatterns = [
   url(r'^agent/', include('agent.urls')),
]
