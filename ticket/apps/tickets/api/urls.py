from django.urls import path

from ticket.apps.tickets.api.views import ImageCreateAPIView
from ticket.apps.tickets.api.views import TicketCreateAPIView

urlpatterns = [
    path("", TicketCreateAPIView.as_view(), name="ticket-create"),
    path("image/", ImageCreateAPIView.as_view(), name="image-create"),
]

app_name = "tickets"
